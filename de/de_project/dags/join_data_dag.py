from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor

from de.de_project.dags.jobs.join_data import append_data_to_database


with DAG(dag_id="join_data_dag",
         schedule_interval="*/3 * * * *",
         catchup=False) as dag:

    task_1 = PythonOperator(
        task_id="join_data",
        python_callable=append_data_to_database
    )

    trigger = ExternalTaskSensor(
        task_id="check_if_imdb_data_needs_to_be_loaded",
        external_dag_id="load_data_to_postgres_dag"
    )

    trigger >> task_1
