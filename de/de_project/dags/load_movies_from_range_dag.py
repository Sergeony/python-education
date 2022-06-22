""" A module with a scheduled DAG, which loads data
from a source to the object storage.
"""
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from de.de_project.dags.jobs.load_movies_from_range import get_movies_from_range
from common import default_args


with DAG("load_movies_from_range_dag",
         default_args=default_args,
         schedule_interval="* 5 * * *",
         catchup=False) as dag:

    task_1 = PythonOperator(
        task_id="load_movies_from_range",
        python_callable=get_movies_from_range,
        op_kwargs={"min_date": datetime.now() - timedelta(days=7),
                   "max_date": datetime.now() - timedelta(days=3)}
    )
