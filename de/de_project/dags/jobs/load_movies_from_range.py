""" A module with a job, which loads data
in the specified time range.
"""
from datetime import datetime
from os import getenv
from json import dumps

from requests import get

from .common import s3


def get_movies_on_page(page, movie_jsons):
    """ Get all movies on the current page.

    - Save only those that have imdb_id and at least one genre
    """
    for movie in page["results"]:
        url = (f"https://api.themoviedb.org/3/movie/{movie['id']}?"
               f"api_key={getenv('API_KEY')}")

        movie_json = get(url).json()

        if movie_json['imdb_id'] and movie_json['genres']:
            movie_jsons.append(movie_json)


def get_movies_from_range(min_date: str, max_date: str):
    """ Get all movies in range.

    - Get number of pages with response.
    - Collect all movies to the list.
    - Load data to the minio.
    """
    url = ("https://api.themoviedb.org/3/discover/movie?"
           f"api_key={getenv('API_KEY')}&"
           f"primary_release_date.gte={min_date}&"
           f"primary_release_date.lte={max_date}")

    page_count = get(url).json()['total_pages']

    movie_jsons = []
    for page_number in range(1, page_count + 1):
        page = get(url + f"&page={page_number}").json()
        get_movies_on_page(page, movie_jsons)
    serialized_data = dumps(movie_jsons)

    if s3.Bucket("raw-movies") not in s3.buckets.all():
        s3.create_bucket(Bucket="raw-movies")

    s3.Bucket("raw-movies").put_object(Key=f"batch-{datetime.now()}.json",
                                       Body=serialized_data)
