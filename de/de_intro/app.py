""" A simple app, which loads the data to the database.
"""
from os import getenv
from sys import argv
from minio import Minio
import pandas as pd
import pandas.core.frame
from sqlalchemy import create_engine


def download_from_minio_to_pd(bucket_name):
    """ Upload the data from the storage into the dataframe.
    """
    client = Minio(
        's3:9000',
        access_key=getenv('S3_USER'),
        secret_key=getenv('S3_PSWD'),
        secure=False
    )

    stock_files = []

    for item in client.list_objects(bucket_name, recursive=True):
        file = client.get_object(bucket_name, item.object_name, item.object_name)
        stock_files.append(file)

    return pd.concat((pd.read_csv(file) for file in stock_files))


def rename_columns(dataframe: pandas.core.frame.DataFrame):
    """ Translate columns to English.
    """
    dataframe.rename(
        inplace=True,
        columns={
            "data": "date",
            "stato": "state",
            "codice_regione": "region_code",
            "denominazione_regione": "region_name",
            "codice_provincia": "province_code",
            "denominazione_provincia": "province_name",
            "sigla_provincia": "province_abbreviation",
            "lat": "latitude",
            "long": "longitude",
            "totale_casi": "cases_total",
            "codice_nuts_1": "nuts_code_1",
            "codice_nuts_2": "nuts_code_2",
            "codice_nuts_3": "nuts_code_3",
        }
    )


def cast_columns(dataframe: pandas.core.frame.DataFrame):
    """ Convert types as specified in the documentation.
    """
    dataframe = dataframe.convert_dtypes()
    dataframe['date'] = pd.to_datetime(dataframe['date'], format='%Y-%m-%d')
    return dataframe


def load_to_db(dataframe: pandas.core.frame.DataFrame):
    """ Create table & insert data to the database.
    """
    engine = create_engine(f'postgresql+psycopg2://'
                           f'{getenv("DB_USER")}:'
                           f'{getenv("DB_PSWD")}'
                           f'@{getenv("DB_CNTR")}:5432/'
                           f'{getenv("DB_NAME")}')

    dataframe.to_sql('ita_covid', con=engine)


def main():
    """ Get all the data, process it and load it into the database.
    """
    dataframe = download_from_minio_to_pd(argv[1])

    rename_columns(dataframe)

    dataframe = cast_columns(dataframe)

    load_to_db(dataframe)


if __name__ == '__main__':
    main()
