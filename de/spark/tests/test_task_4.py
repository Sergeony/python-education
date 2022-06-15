""" Unit tests for task_4

There are tests for each unit in task_4.py
"""
from pyspark.sql.types import Row

from de.spark.tests.utils import dfs_equal
from de.spark.task_4 import get_top_actors
from de.spark.task_1 import get_top


def test_get_top_actors(spark_session, movie_df, rating_df, principals_df, names_df):
    """ Test for get_top_actors

    - Using fixtures on principals, names df-s and top_movies df,
    compare an expected df with actual one.
    """
    expected_df = spark_session.createDataFrame([
        Row(primaryName='John Travolta'),
        Row(primaryName='Clint Eastwood'),
        Row(primaryName='James Franko'),
        Row(primaryName='Samuel Jackson'),
        Row(primaryName='Andrew Garfield'),
    ])

    top_movies = get_top(movie_df, rating_df)
    actual_df = get_top_actors(top_movies, principals_df, names_df)

    assert dfs_equal(actual_df, expected_df)
