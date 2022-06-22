from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from common import default_args
from de.de_project.dags.jobs.load_movies_from_range import get_movies_from_range

with DAG("load_latest_movies_dag",
         default_args=default_args,
         schedule_interval="* * * * *",
         catchup=False) as dag:

    task_1 = PythonOperator(
        task_id="load_latest_movies",
        python_callable=get_movies_from_range,
        op_kwargs={"min_date": datetime.now() - timedelta(days=1),
                   "max_date:": datetime.now()}
    )
