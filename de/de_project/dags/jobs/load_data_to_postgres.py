""" A module with a job, which loads data from
the object storage to the database.
"""
from os import getenv
from functools import reduce

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from pyspark.sql import DataFrame
import pyspark.sql.functions as f

from de.de_project.dags.common import s3, sc, spark_session


def get_database():
    """ Get database instance.

    - Connect to the postgres and check, if database exists.
    - Create it, if not and return the instance.
    """
    postgres_url = 'postgresql://' \
                   f'{getenv("POSTGRES_USER")}:' \
                   f'{getenv("POSTGRES_PASSWORD")}' \
                   f'@postgres:5432'

    db_url = postgres_url + f'/{getenv("POSTGRES_DB")}'

    postgres = create_engine(postgres_url).connect()

    if not database_exists(db_url):
        create_database(db_url)

    database = create_engine(db_url)

    postgres.close()

    return database


def get_df():
    """ Create dataframe from the stored objects.

    - Load each object and turn it to dataframe.
    - Union them after all.
    - Separate rows on genre and drop duplicate ones.
    """
    dfs = []
    for json_obj in s3.Bucket("movies").objects.all():
        file = json_obj.get()["Body"].read().decode("utf-8")
        movie_df = spark_session.read.json(sc.parallelize([file]))
        dfs.append(movie_df)
    movie_df = reduce(DataFrame.unionAll, dfs)

    movie_df = movie_df.select('id',
                               'imdb_id',
                               f.explode(f.split(f.col('genres'), ',')).alias('genre'))

    return movie_df.drop_duplicates()


def load_data_to_postgres():
    """ Load data to the postgres database.

    - Get dataframe from the minio.
    - After all, delete all stored objects.
    - Create table, if not exists.
    - Finally, load dataframe to the database.
    """
    movie_df = get_df()
    s3.Bucket("movies").objects.all().delete()

    database = get_database().connect()

    database.execute("CREATE TABLE IF NOT EXISTS movies ("
                     "id INT PRIMARY KEY,"
                     "imdb_id VARCHAR NOT NULL,"
                     "genre VARCHAR NOT NULL );")

    movie_df.to_pandas_on_spark().to_pandas().to_sql("movies",
                                                     con=database,
                                                     if_exists='append',
                                                     index=False)

    database.close()
