from de.de_project.dags.jobs.load_data_to_postgres import get_database
from de.de_project.dags.common import s3, spark_session


def get_ratings_df():
    # response = get("https://datasets.imdbws.com/title.ratings.tsv.gz").text.encode('utf-8')

    rating_obj = s3.Bucket("movies").Object(bucket_name="movies",
                                            key="data.tsv")

    return spark_session.read.options(delimiter='\t').csv(rating_obj.get()["Body"])


def append_data_to_database():
    df = get_ratings_df()

    database = get_database().connect()

    database.execute("CREATE TEMPORARY TABLE additional_data ("
                      "averageRating FLOAT NOT NULL"
                      "numVotes INT NOT NULL );")

    df.to_pandas_on_spark().to_pandas().to_sql("additional_data",
                                               con=database,
                                               index=False)

    database.execute("ALTER TABLE movies"
                      "ADD COLUMN IF NOT EXISTS average_rating FLOAT"
                      "ADD COLUMN IF NOT EXISTS num_votes INT")

    database.execute('UPDATE movies'
                      'SET average_rating=additional_data."averageRating",'
                      'SET num_votes=numVotes')

    database.close()
