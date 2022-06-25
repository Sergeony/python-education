from pytest import fixture
from pyspark.sql import SparkSession, Row


@fixture(scope='session', autouse=True)
def spark_session():
    """Fixture that enables SparkSession during tests run.

    Yields:
        SparkSession: current SparkSession
    """
    spark_session = SparkSession.builder.getOrCreate()
    spark_session.conf.set("spark.sql.session.timeZone", "UTC")

    yield spark_session

    spark_session.sparkContext.stop()


@fixture(scope='session', autouse=True)
def movie_df(spark_session):
    """ Example of a movie df
    """
    return spark_session.createDataFrame([
        Row(tconst='1', primaryTitle='Something 1', startYear='2012', genre='Action'),
        Row(tconst='2', primaryTitle='Something 2', startYear='2011', genre='Action'),
        Row(tconst='3', primaryTitle='Something 3', startYear='2021', genre='Action'),
        Row(tconst='4', primaryTitle='Something 4', startYear='2022', genre='Comedy'),
        Row(tconst='5', primaryTitle='Something old 1', startYear='1959', genre='Comedy'),
        Row(tconst='6', primaryTitle='Something old 2', startYear='1960', genre='Comedy'),
        Row(tconst='7', primaryTitle='Something old 3', startYear='1964', genre='Adventure'),
        Row(tconst='8', primaryTitle='Something old 4', startYear='1969', genre='Adventure'),
        Row(tconst='9', primaryTitle='Something old 5', startYear='1970', genre='Adventure'),
    ])


@fixture(scope='session', autouse=True)
def rating_df(spark_session):
    """ Example of a rating df
    """
    return spark_session.createDataFrame([
        Row(tconst='1', averageRating=10, numVotes=90_000),
        Row(tconst='2', averageRating=9, numVotes=100_020),
        Row(tconst='3', averageRating=8, numVotes=120_000),
        Row(tconst='4', averageRating=9, numVotes=130_000),
        Row(tconst='5', averageRating=7, numVotes=100_005),
        Row(tconst='6', averageRating=8, numVotes=100_100),
        Row(tconst='7', averageRating=6, numVotes=110_000),
        Row(tconst='8', averageRating=9, numVotes=100_001),
        Row(tconst='9', averageRating=5, numVotes=150_000),
    ])


@fixture(scope='session', autouse=True)
def principals_df(spark_session):
    """ Example of a principals df
    """
    return spark_session.createDataFrame([
        Row(tconst='1', nconst='1'),
        Row(tconst='1', nconst='3'),
        Row(tconst='2', nconst='2'),
        Row(tconst='2', nconst='4'),
        Row(tconst='3', nconst='1'),
        Row(tconst='3', nconst='5'),
        Row(tconst='4', nconst='3'),
        Row(tconst='4', nconst='5'),
        Row(tconst='5', nconst='2'),
        Row(tconst='5', nconst='4'),
        Row(tconst='6', nconst='1'),
        Row(tconst='6', nconst='4'),
        Row(tconst='7', nconst='1'),
        Row(tconst='7', nconst='5'),
        Row(tconst='8', nconst='3'),
        Row(tconst='8', nconst='1'),
        Row(tconst='9', nconst='5'),
        Row(tconst='9', nconst='2'),
    ])


@fixture(scope='session', autouse=True)
def names_df(spark_session):
    """ Example of a names df
    """
    return spark_session.createDataFrame([
        Row(nconst='1', primaryName='John Travolta'),
        Row(nconst='2', primaryName='James Franko'),
        Row(nconst='3', primaryName='Andrew Garfield'),
        Row(nconst='4', primaryName='Samuel Jackson'),
        Row(nconst='5', primaryName='Clint Eastwood'),
    ])
