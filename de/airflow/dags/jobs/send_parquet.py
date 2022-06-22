from os import getenv
from datetime import datetime
from io import BytesIO
from functools import reduce

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.functions import col, lower, to_timestamp
from boto3 import session


spark_context = SparkContext(master="local[*]",
                             appName="send_parquet")


spark_session = (SparkSession.builder
                             .master('local')
                             .appName('send_parquet')
                             .config(conf=SparkConf())
                             .getOrCreate())


s3 = session.Session().resource(
    service_name="s3",
    endpoint_url="http://s3:9000",
    aws_access_key_id=getenv("MINIO_ROOT_USER"),
    aws_secret_access_key=getenv("MINIO_ROOT_PASSWORD")
)


def load_from_s3_to_df(bucket_name):

    dfs = []
    for json_obj in s3.Bucket(bucket_name).objects.all():
        json = json_obj.get()["Body"].read().decode("utf-8")
        df = spark_session.read.json(spark_context.parallelize([json]))
        dfs.append(df)

    return reduce(DataFrame.unionAll, dfs)


def clear_buckets():
    for bucket in s3.buckets.all():
        bucket.objects.all().delete()


def process_data():
    result_df = transform_bitfinex()
    result_df = result_df.union(transform_bitmex())
    result_df = result_df.union(transform_poloniex())

    clear_buckets()

    if not s3.Bucket('processed-data') in s3.buckets.all():
        s3.create_bucket(Bucket='processed-data')

    with BytesIO() as buffer:
        result_df.toPandas().to_parquet(buffer, index=False)

        s3.Bucket('processed-data').put_object(Key=f'batch-{datetime.now()}.parquet',
                                               Body=buffer.getvalue())


def transform_bitfinex():
    df = load_from_s3_to_df('bitfinex')

    return df.select(to_timestamp(col("timestamp")).alias("time"),
                     col("tid").alias("ID"),
                     col("amount"),
                     col("type"),
                     col("price"))


def transform_bitmex():
    df = load_from_s3_to_df('bitmex')

    return df.select(to_timestamp(col("timestamp")).alias("time"),
                     col("trdMatchID").alias("ID"),
                     col("homeNotional").alias("amount"),
                     lower(col("side")).alias("type"),
                     col("price"))


def transform_poloniex():
    df = load_from_s3_to_df('poloniex')

    return df.select(to_timestamp(col("date")).alias("time"),
                     col("globalTradeID").alias("ID"),
                     col("amount"),
                     col("type"),
                     col("rate").alias("price"))


if __name__ == "__main__":
    process_data()
