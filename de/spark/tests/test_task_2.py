""" Unit tests for task_2

There are tests for each unit in task_2.py
"""
from pyspark.sql.types import Row

from de.spark.tests.utils import dfs_equal
from de.spark.task_2 import get_top_10_for_each_genre


def test_get_top_10_for_each_genre(spark_session, movie_df, rating_df):
    """ Test for get_top_10_for_each_genre

    - Using fixtures on movie and rating df-s,
    compare an expected df with actual one.
    """
    expected_df = spark_session.createDataFrame([
        Row(tconst='2', primaryTitle='Something 2', startYear='2011', genre='Action', averageRating=9,
            numVotes=100_020),
        Row(tconst='3', primaryTitle='Something 3', startYear='2021', genre='Action', averageRating=8,
            numVotes=120_000),
        Row(tconst='8', primaryTitle='Something old 4', startYear='1969', genre='Adventure', averageRating=9,
            numVotes=100_001),
        Row(tconst='7', primaryTitle='Something old 3', startYear='1964', genre='Adventure', averageRating=6,
            numVotes=110_000),
        Row(tconst='9', primaryTitle='Something old 5', startYear='1970', genre='Adventure', averageRating=5,
            numVotes=150_000),
        Row(tconst='4', primaryTitle='Something 4', startYear='2022', genre='Comedy', averageRating=9,
            numVotes=130_000),
        Row(tconst='6', primaryTitle='Something old 2', startYear='1960', genre='Comedy', averageRating=8,
            numVotes=100_100),
        Row(tconst='5', primaryTitle='Something old 1', startYear='1959', genre='Comedy', averageRating=7,
            numVotes=100_005),
    ])
    actual_df = get_top_10_for_each_genre(movie_df, rating_df)

    assert dfs_equal(actual_df, expected_df)
