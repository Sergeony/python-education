""" A module with a job, which
loads data from the object storage to the database.
"""
from io import BytesIO

import pandas as pd

from .load_data_to_postgres import get_database
from .common import s3


def get_ratings_df():
    """ Create dataframe from the file in the object storage.
    """
    rating_obj = s3.Object("imdb-data", "data.tsv")

    file = rating_obj.get()["Body"].read()

    return pd.read_csv(BytesIO(file), sep='\t')


def add_data_to_database():
    """ Add loaded data to the database.

    - Get dataframe from the imdb data.
    - Connect to the database.
    - Create and fill table with imdb data.
    - Update main table with data in imdb table.
    - Delete table with imdb data.
    """
    rating_df = get_ratings_df()

    database = get_database()

    # TODO: replace pandas on spark
    rating_df.to_sql("additional_data", con=database, index=False)

    database.execute('ALTER TABLE movies '
                     'ADD COLUMN IF NOT EXISTS average_rating DOUBLE PRECISION, '
                     'ADD COLUMN IF NOT EXISTS num_votes BIGINT')

    database.execute('UPDATE movies SET '
                     'average_rating = additional_data."averageRating", '
                     'num_votes = additional_data."numVotes" '
                     'FROM additional_data '
                     'WHERE movies.imdb_id = additional_data."tconst"')

    database.execute('DROP TABLE IF EXISTS additional_data')
