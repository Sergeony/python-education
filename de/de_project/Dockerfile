# syntax=docker/Dockerfile:1

FROM apache/airflow:2.2.0-python3.8

WORKDIR /app

COPY requirements.txt /app
COPY airflow.cfg /app
COPY entrypoint.sh /app

RUN pip install --upgrade pip==22.1.2
RUN pip install -r /app/requirements.txt

COPY dags /app/dags
COPY dags/jobs /app/jobs

ENTRYPOINT [ "sh", "/app/entrypoint.sh" ]
