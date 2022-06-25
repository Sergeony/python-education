""" Unit tests for task_3

There are tests for each unit in task_3.py
"""
from pyspark.sql.types import Row

from de.spark.tests.utils import dfs_equal
from de.spark.task_3 import get_top_10_for_each_genre_in_decade


def test_get_top_10_for_each_genre_in_decade(spark_session, movie_df, rating_df):
    """ Test for get_top_10_for_each_genre

    - Using fixtures on movie and rating df-s,
    compare an expected df with actual one.
    """
    expected_df = spark_session.createDataFrame([
        Row(tconst='3', primaryTitle='Something 3', startYear='2021', genre='Action', yearRange='2020-2030',
            averageRating=8, numVotes=120_000),
        Row(tconst='4', primaryTitle='Something 4', startYear='2022', genre='Comedy', yearRange='2020-2030',
            averageRating=9, numVotes=130_000),
        Row(tconst='2', primaryTitle='Something 2', startYear='2011', genre='Action', yearRange='2010-2020',
            averageRating=9, numVotes=100_020),
        Row(tconst='9', primaryTitle='Something old 5', startYear='1970', genre='Adventure', yearRange='1970-1980',
            averageRating=5, numVotes=150_000),
        Row(tconst='8', primaryTitle='Something old 4', startYear='1969', genre='Adventure', yearRange='1960-1970',
            averageRating=9, numVotes=100_001),
        Row(tconst='7', primaryTitle='Something old 3', startYear='1964', genre='Adventure', yearRange='1960-1970',
            averageRating=6, numVotes=110_000),
        Row(tconst='6', primaryTitle='Something old 2', startYear='1960', genre='Comedy', yearRange='1960-1970',
            averageRating=8, numVotes=100_100),
        Row(tconst='5', primaryTitle='Something old 1', startYear='1959', genre='Comedy',  yearRange='1950-1960',
            averageRating=7, numVotes=100_005),
    ])
    actual_df = get_top_10_for_each_genre_in_decade(movie_df, rating_df)

    assert dfs_equal(actual_df, expected_df)
