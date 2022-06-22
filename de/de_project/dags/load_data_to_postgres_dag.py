""" A module with a scheduled DAG, which loads
data from the object storage to the database.
"""
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor

from de.de_project.dags.jobs.load_data_to_postgres import load_data_to_postgres
from common import default_args


with DAG("load_data_to_postgres_dag",
         default_args=default_args,
         schedule_interval="*/2 * * * *",
         catchup=False):

    sensor_1 = ExternalTaskSensor(
        task_id="triggers_on_daily_loaded_data",
        external_dag_id="load_latest_movies_dag"
    )

    task_1 = PythonOperator(
        task_id="load_data_to_postgres",
        python_callable=load_data_to_postgres
    )

    sensor_1 >> task_1
