from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor

from de.de_project.dags.jobs.load_data_to_postgres import load_data_to_postgres
from common import default_args


with DAG("load_data_to_postgres_dag",
         default_args=default_args,
         schedule_interval="*/2 * * * *",
         catchup=False):

    task_1 = PythonOperator(
        task_id="load_data_to_postgres",
        python_callable=load_data_to_postgres
    )
