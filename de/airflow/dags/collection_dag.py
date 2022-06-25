from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

from jobs.get_rates import main


default_args = {
    "owner": "admin",
    "depends_on_past": False,
    "start_date": datetime(2021, 1, 2, 0, 0, 0),
    "email": ["my_email@gmail.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 0,
    "retry_delay": timedelta(minutes=1)
}


with DAG(dag_id="push_json_minio",
         default_args=default_args,
         schedule_interval='* * * * *',
         catchup=False) as dag:

    task_1 = PythonOperator(
        task_id="get_stat_bitfinex", python_callable=main
    )
