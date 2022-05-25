# syntax=docker/Dockerfile:1

FROM python:3.8-slim-buster
WORKDIR /app
COPY app.py ./
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
CMD [ "python3", "./app.py", "test-bucket","--host=0.0.0.0"]
