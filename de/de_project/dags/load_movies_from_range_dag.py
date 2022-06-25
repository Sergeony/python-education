""" A module with a demand DAG, which loads data
from a source to the object storage.
"""
from datetime import date, timedelta

from airflow.operators.python import PythonOperator
from airflow import DAG

from jobs.load_movies_from_range import get_movies_from_range
from jobs.common import default_args


with DAG(dag_id="load_movies_from_range_dag",
         default_args=default_args,
         schedule_interval=None,
         catchup=False) as dag:

    task_1 = PythonOperator(
        task_id="load_movies_from_range",
        python_callable=get_movies_from_range,
        op_kwargs={"min_date": str(date.today() - timedelta(days=7)),
                   "max_date": str(date.today() - timedelta(days=3))})
