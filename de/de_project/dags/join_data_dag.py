""" A module with a scheduled DAG, which joins imdb data with data in the database.
Depends on the database DAG.
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor

from jobs.join_data import add_data_to_database
from jobs.common import default_args


with DAG(dag_id="join_data_dag",
         default_args=default_args,
         schedule_interval="*/10 * * * *",
         catchup=False) as dag:

    sensor_1 = ExternalTaskSensor(
        task_id="check_if_imdb_data_needs_to_be_loaded",
        external_dag_id="load_data_to_postgres_dag",
        external_task_id="load_data_to_postgres")

    task_1 = PythonOperator(
        task_id="join_data",
        python_callable=add_data_to_database)

    sensor_1 >> task_1
