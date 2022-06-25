""" A module with a job, which loads data from
the object storage to the database.
"""
from os import getenv
from functools import reduce

from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from pyspark.sql import DataFrame
import pyspark.sql.functions as f

from .common import s3, sc, spark_session


def get_database():
    """ Get database instance.

    - Create it, if not exists.
    """
    url = ('postgresql://'
           f'{getenv("POSTGRES_USER")}:'
           f'{getenv("POSTGRES_PASSWORD")}@'
           'postgres:5432/'
           f'{getenv("MOVIE_DB")}')

    if not database_exists(url):
        create_database(url)

    return create_engine(url)


def get_df() -> DataFrame:
    """ Create dataframe from the stored objects.

    - Load each object to dataframe and merge them to one.
    - Keep only the required cols and only the first genre.
    """
    dfs = []
    for json_obj in s3.Bucket("raw-movies").objects.all():
        file = json_obj.get()["Body"].read().decode("utf-8")
        movie_df = spark_session.read.json(sc.parallelize([file]))
        dfs.append(movie_df)

    movie_df = reduce(DataFrame.unionAll, dfs)

    return movie_df.select('id',
                           'imdb_id',
                           (f.col('genres').getItem(0)['name']).alias('genre'))


def load_data_to_postgres():
    """ Load data to the postgres database.

    - Load dataframe to the database.
    - Delete all stored objects.
    """
    movie_df = get_df().to_pandas_on_spark().to_pandas()

    # TODO: replace pandas on spark
    movie_df.to_sql("movies",
                    con=get_database(),
                    if_exists='append',
                    index=False)

    s3.Bucket("raw-movies").objects.all().delete()
