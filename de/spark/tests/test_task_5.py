""" Unit tests for task_5

There are tests for each unit in task_5.py
"""
from pyspark.sql.types import Row

from de.spark.tests.utils import dfs_equal
from de.spark.task_5 import get_top_5_movies_for_each_director


def test_get_top_5_movies_for_each_director(spark_session, movie_df, rating_df, names_df, principals_df):
    """ Test for get_top_5_movies_for_each_director

    - Using fixtures on movie, rating,
    names and principals df-s
    compare an expected df with actual one.
    """
    expected_df = spark_session.createDataFrame([
        Row(nconst='3', tconst='1', primaryTitle='Something 1', startYear='2012', genre='Action', averageRating=10,
            numVotes=90_000, primaryName='Andrew Garfield'),
        Row(nconst='3', tconst='4', primaryTitle='Something 4', startYear='2022', genre='Comedy', averageRating=9,
            numVotes=130_000, primaryName='Andrew Garfield'),
        Row(nconst='3', tconst='8', primaryTitle='Something old 4', startYear='1969', genre='Adventure', averageRating=9,
            numVotes=100_001, primaryName='Andrew Garfield'),
        Row(nconst='5', tconst='4', primaryTitle='Something 4', startYear='2022', genre='Comedy', averageRating=9,
            numVotes=130_000, primaryName='Clint Eastwood'),
        Row(nconst='5', tconst='3', primaryTitle='Something 3', startYear='2021', genre='Action', averageRating=8,
            numVotes=120_000, primaryName='Clint Eastwood'),
        Row(nconst='5', tconst='7', primaryTitle='Something old 3', startYear='1964', genre='Adventure', averageRating=6,
            numVotes=110_000, primaryName='Clint Eastwood'),
        Row(nconst='5', tconst='9', primaryTitle='Something old 5', startYear='1970', genre='Adventure', averageRating=5,
            numVotes=150_000, primaryName='Clint Eastwood'),
        Row(nconst='2', tconst='2', primaryTitle='Something 2', startYear='2011', genre='Action', averageRating=9,
            numVotes=100_020, primaryName='James Franko'),
        Row(nconst='2', tconst='5', primaryTitle='Something old 1', startYear='1959', genre='Comedy', averageRating=7,
            numVotes=100_005, primaryName='James Franko'),
        Row(nconst='2', tconst='9', primaryTitle='Something old 5', startYear='1970', genre='Adventure', averageRating=5,
            numVotes=150_000, primaryName='James Franko'),
        Row(nconst='1', tconst='1', primaryTitle='Something 1', startYear='2012', genre='Action', averageRating=10,
            numVotes=90_000, primaryName='John Travolta'),
        Row(nconst='1', tconst='8', primaryTitle='Something old 4', startYear='1969', genre='Adventure', averageRating=9,
            numVotes=100_001, primaryName='John Travolta'),
        Row(nconst='1', tconst='3', primaryTitle='Something 3', startYear='2021', genre='Action', averageRating=8,
            numVotes=120_000, primaryName='John Travolta'),
        Row(nconst='1', tconst='6', primaryTitle='Something old 2', startYear='1960', genre='Comedy', averageRating=8,
            numVotes=100_100, primaryName='John Travolta'),
        Row(nconst='1', tconst='7', primaryTitle='Something old 3', startYear='1964', genre='Adventure', averageRating=6,
            numVotes=110_000, primaryName='John Travolta'),
        Row(nconst='4', tconst='2', primaryTitle='Something 2', startYear='2011', genre='Action', averageRating=9,
            numVotes=100_020, primaryName='Samuel Jackson'),
        Row(nconst='4', tconst='6', primaryTitle='Something old 2', startYear='1960', genre='Comedy', averageRating=8,
            numVotes=100_100, primaryName='Samuel Jackson'),
        Row(nconst='4', tconst='5', primaryTitle='Something old 1', startYear='1959', genre='Comedy', averageRating=7,
            numVotes=100_005, primaryName='Samuel Jackson'),
    ])
    actual_df = get_top_5_movies_for_each_director(movie_df, rating_df, names_df, principals_df)

    assert dfs_equal(actual_df, expected_df)
