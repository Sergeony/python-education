""" A module to find top movies with different filters.
"""
from datetime import datetime
from pyspark import SparkConf
from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as f


def create_session() -> SparkSession:
    """ Just create a new spark session.
    """
    return (SparkSession.builder
                        .master('local')
                        .appName('task app')
                        .config(conf=SparkConf())
                        .getOrCreate())


def create_rating_df(session: SparkSession) -> DataFrame:
    """ Create and prepare rating dataframe for the task.
    """
    rating_df = session.read.options(delimiter='\t').csv('input_data/ratings.tsv', header=True)

    rating_df = rating_df.select('tconst',
                                 'averageRating',
                                 'numVotes')

    rating_df = rating_df.withColumn('averageRating', rating_df.averageRating.cast('double'))
    rating_df = rating_df.withColumn('numVotes', rating_df.numVotes.cast('int'))

    return rating_df


def create_movie_df(session: SparkSession) -> DataFrame:
    """ Create and prepare movie dataframe for the task.
    """
    movie_df = session.read.options(delimiter='\t').csv('input_data/titles.tsv', header=True)

    movie_df = movie_df.where(f.col('titleType') == 'movie')

    movie_df = movie_df.select('tconst',
                               'primaryTitle',
                               'startYear')

    return movie_df


def get_top(movie_df: DataFrame, rating_df: DataFrame) -> DataFrame:
    """ Get top 100 movies with more than 100000 votes.
    """
    movie_df = movie_df.select('tconst',
                               'primaryTitle')

    return (movie_df.join(rating_df, on='tconst')
                    .where(f.col('numVotes') >= 100_000)
                    .orderBy('averageRating', ascending=False)
                    .limit(100))


def get_top_from_the_last_decade(movie_df: DataFrame, rating_df: DataFrame) -> DataFrame:
    """ Do the same as get_top for films from the last decade.
    """
    movie_df = movie_df.where(f.col('startYear') >= datetime.now().year - 10)

    return get_top(movie_df, rating_df)


def get_top_for_60s(movie_df: DataFrame, rating_df: DataFrame) -> DataFrame:
    """ Do the same as get_top for films released in the 1960s.
    """
    movie_df = movie_df.where(movie_df.startYear.between(1960, 1969))

    return get_top(movie_df, rating_df)


def main():
    """ Complete 3 tasks and save results in files.
    """
    session = create_session()

    rating_df = create_rating_df(session)
    movie_df = create_movie_df(session)

    get_top(movie_df, rating_df).write.csv('output_data/task_1_a.csv',
                                           header=True)

    get_top_from_the_last_decade(movie_df, rating_df).write.csv('output_data/task_1_b.csv',
                                                                header=True)

    get_top_for_60s(movie_df, rating_df).write.csv('output_data/task_1_c.csv',
                                                   header=True)


if __name__ == '__main__':
    main()
