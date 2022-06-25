""" A module with a scheduled DAG, which loads
data from the object storage to the database.
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task import ExternalTaskSensor

from jobs.load_data_to_postgres import load_data_to_postgres
from jobs.common import default_args


with DAG(dag_id="load_data_to_postgres_dag",
         default_args=default_args,
         schedule_interval="*/10 * * * *",
         catchup=False) as dag:

    sensor_1 = ExternalTaskSensor(
        task_id="triggers_on_daily_loaded_data",
        external_dag_id="load_latest_movies_dag",
        external_task_id="load_latest_movies")

    task_1 = PythonOperator(
        task_id="load_data_to_postgres",
        python_callable=load_data_to_postgres)

    sensor_1 >> task_1
