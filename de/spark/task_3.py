""" A module to find top 10 movies for each genre in decades.
"""
from datetime import datetime
from functools import reduce

from pyspark.sql import DataFrame
import pyspark.sql.functions as f

from de.spark.task_1 import create_rating_df, create_session
from de.spark.task_2 import create_movie_df, get_top_10_for_each_genre


def get_top_10_for_each_genre_in_decade(movie_df: DataFrame, rating_df: DataFrame):
    """ Find the top 10 films for each genre in the decade from today to the 1950s.
    """
    decade = datetime.now().year // 10
    tops_in_decade = []

    for decade in range(decade, 194, -1):
        movies_in_decade = (movie_df.where(movie_df.startYear.between(decade*10,
                                                                      decade*10+9))
                                    .withColumn('yearRange',
                                                f.lit(f'{decade*10}-{(decade+1)*10}'))
                            )

        tops_in_decade.append(get_top_10_for_each_genre(movies_in_decade, rating_df))

    return reduce(lambda df_1, df_2: df_1.union(df_2), tops_in_decade)


def main():
    """ Complete the task and save result to the file.
    """
    spark_session = create_session()

    rating_df = create_rating_df(spark_session)
    movie_df = create_movie_df(spark_session)

    get_top_10_for_each_genre_in_decade(movie_df, rating_df).write.csv('output_data/task_3.csv',
                                                                       header=True)


if __name__ == '__main__':
    main()
