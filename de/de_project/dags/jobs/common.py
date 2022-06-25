""" A module with commonly used and default objects for most modules.
"""
from datetime import datetime
from os import getenv

from pyspark import SparkConf, SparkContext
from pyspark.sql import SparkSession
from boto3 import session


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 1, 1, 0, 0, 0),
    "email": ["admin@example.org"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": 0
}


s3 = session.Session().resource(service_name="s3",
                                endpoint_url="http://s3:9000",
                                aws_access_key_id=getenv("MINIO_ROOT_USER"),
                                aws_secret_access_key=getenv("MINIO_ROOT_PASSWORD"))


sc = SparkContext()
spark_session = (SparkSession.builder
                             .master("local")
                             .appName("load_data_to_postgres")
                             .config(conf=SparkConf())
                             .getOrCreate())
