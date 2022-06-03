""" A module to find top actors.
"""
from pyspark.sql import SparkSession, DataFrame
import pyspark.sql.functions as f
from task_1 import create_session, get_top, create_rating_df, create_movie_df


def create_principals_df(session: SparkSession) -> DataFrame:
    """ Create and prepare principals dataframe for the task.
    """
    principals_df = session.read.options(delimiter='\t').csv('input_data/principals.tsv',
                                                             header=True)

    principals_df = (principals_df.where((f.col('category') == 'actor') |
                                         (f.col('category') == 'actress'))
                                  .select('tconst',
                                          'nconst'))

    return principals_df


def create_names_df(session: SparkSession) -> DataFrame:
    """ Create and prepare actors dataframe for the task.
    """
    names_df = session.read.options(delimiter='\t').csv('input_data/names.tsv',
                                                        header=True)

    names_df = names_df.select('nconst',
                               'primaryName')

    return names_df


def get_top_actors(top_movies: DataFrame,
                   principals_df: DataFrame,
                   actors_df: DataFrame) -> DataFrame:
    """ Find actors who starred in the top 100 movies more than 1 time.
    """
    return (top_movies.join(principals_df, on='tconst')
                      .join(actors_df, on='nconst')
                      .groupby('primaryName')
                      .agg(f.count('nconst').alias('film_count'))
                      .where(f.col('film_count') > 1)
                      .orderBy(f.col('film_count'),
                               ascending=False)
                      .select('primaryName'))


def main():
    """ Complete the task and save result to the file.
    """
    session = create_session()

    rating_df = create_rating_df(session)
    movie_df = create_movie_df(session)
    names_df = create_names_df(session)
    principals_df = create_principals_df(session)

    top_movies = get_top(movie_df, rating_df)

    get_top_actors(top_movies, principals_df, names_df).write.csv('output_data/task_4.csv',
                                                                  header=True)


if __name__ == '__main__':
    main()
