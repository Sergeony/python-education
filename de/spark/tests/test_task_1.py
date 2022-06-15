""" Unit tests for task_1

There are tests for each unit in task_1.py
"""
from pyspark.sql.types import Row

from de.spark.tests.utils import dfs_equal
from de.spark.task_1 import get_top, get_top_from_the_last_decade, get_top_for_60s


def test_get_top(spark_session, movie_df, rating_df):
    """ Test for get_top

    - Using fixtures on movie and rating df-s,
    compare an expected df with actual one.
    """
    expected_df = spark_session.createDataFrame([
        Row(tconst='8', primaryTitle='Something old 4', averageRating=9, numVotes=100_001),
        Row(tconst='2', primaryTitle='Something 2', averageRating=9, numVotes=100_020),
        Row(tconst='4', primaryTitle='Something 4', averageRating=9, numVotes=130_000),
        Row(tconst='3', primaryTitle='Something 3', averageRating=8, numVotes=120_000),
        Row(tconst='6', primaryTitle='Something old 2', averageRating=8, numVotes=100_100),
        Row(tconst='5', primaryTitle='Something old 1', averageRating=7, numVotes=100_005),
        Row(tconst='7', primaryTitle='Something old 3', averageRating=6, numVotes=110_000),
        Row(tconst='9', primaryTitle='Something old 5', averageRating=5, numVotes=150_000),
    ])
    actual_df = get_top(movie_df, rating_df)

    assert dfs_equal(actual_df, expected_df)


def test_get_top_from_the_last_decade(spark_session, movie_df, rating_df):
    """ Test for get_top_from_the_last_decade

    - Using fixtures on movie and rating df-s,
    compare an expected df with actual one.
    """
    expected_df = spark_session.createDataFrame([
        Row(tconst='4', primaryTitle='Something 4', averageRating=9, numVotes=130_000),
        Row(tconst='3', primaryTitle='Something 3', averageRating=8, numVotes=120_000),
    ])
    actual_df = get_top_from_the_last_decade(movie_df, rating_df)

    assert dfs_equal(actual_df, expected_df)


def test_get_top_for_60s(spark_session, movie_df, rating_df):
    """ Test for get_top_for_60s

    - Using fixtures on movie and rating df-s,
    compare an expected df with actual one.
    """
    expected_df = spark_session.createDataFrame([
        Row(tconst='6', primaryTitle='Something old 2', averageRating=8, numVotes=100_100),
        Row(tconst='7', primaryTitle='Something old 3', averageRating=6, numVotes=110_000),
        Row(tconst='8', primaryTitle='Something old 4', averageRating=9, numVotes=100_001),
    ])
    actual_df = get_top_for_60s(movie_df, rating_df)

    assert dfs_equal(actual_df, expected_df)
