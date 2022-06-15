""" A module that finds top 5 movies for each director.
"""
from pyspark.sql import SparkSession, DataFrame, Window
import pyspark.sql.functions as f

from de.spark.task_1 import create_session, create_rating_df, create_movie_df
from de.spark.task_4 import create_names_df


def create_principals_df(session: SparkSession) -> DataFrame:
    """ Create and prepare principals dataframe for the task.
    """
    principals_df = session.read.options(delimiter='\t').csv('input_data/principals.tsv',
                                                             header=True)

    principals_df = (principals_df.where(f.col('category') == 'director')
                                  .select('tconst',
                                          'nconst'))

    return principals_df


def get_top_5_movies_for_each_director(movie_df: DataFrame,
                                       rating_df: DataFrame,
                                       names_df: DataFrame,
                                       principals_df: DataFrame) -> DataFrame:
    """ Find top 5 movies for each director.
    """
    window_spec = Window.orderBy(f.desc('averageRating')).partitionBy('primaryName')

    return (movie_df.join(rating_df, on='tconst')
                    .join(principals_df, on='tconst')
                    .join(names_df, on='nconst')
                    .withColumn('r_num',
                                f.row_number().over(window_spec)).where(f.col('r_num') < 6)
                    .drop('r_num'))


def main():
    """ Complete the task and save result to the file.
    """
    session = create_session()

    rating_df = create_rating_df(session)
    movie_df = create_movie_df(session)
    names_df = create_names_df(session)
    principals_df = create_principals_df(session)

    get_top_5_movies_for_each_director(movie_df,
                                       rating_df,
                                       names_df,
                                       principals_df).write.csv('output_data/task_5.csv',
                                                                header=True)


if __name__ == '__main__':
    main()
