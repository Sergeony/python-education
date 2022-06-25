""" A module that finds top 10 movies for each genre.
"""
from pyspark.sql import Window, SparkSession
import pyspark.sql.functions as f
from pyspark.sql import DataFrame

from de.spark.task_1 import create_session, create_rating_df


def create_movie_df(session: SparkSession) -> DataFrame:
    """ Create and prepare movie dataframe for the task.
    """
    movie_df = session.read.options(delimiter='\t').csv('input_data/titles.tsv', header=True)

    movie_df = movie_df.where(f.col('titleType') == 'movie')

    movie_df = movie_df.select('tconst',
                               'primaryTitle',
                               'startYear',
                               f.explode(f.split(f.col('genres'), ',')).alias('genre'))

    return movie_df


def get_top_10_for_each_genre(movie_df: DataFrame, rating_df: DataFrame) -> DataFrame:
    """ Find top 10 movies for each genre.
    """
    window_spec = Window.orderBy(f.desc('averageRating')).partitionBy('genre')

    return (movie_df.join(rating_df, on='tconst')
                    .where(f.col('numVotes') > 100_000)
                    .withColumn('r_num',
                                f.row_number().over(window_spec)).where(f.col('r_num') < 11)
                    .drop('r_num'))


def main():
    """ Complete the task and save result to the file.
    """
    spark_session = create_session()

    rating_df = create_rating_df(spark_session)
    movie_df = create_movie_df(spark_session)

    get_top_10_for_each_genre(movie_df, rating_df).write.csv('output_data/task_2.csv',
                                                             header=True)


if __name__ == '__main__':
    main()
