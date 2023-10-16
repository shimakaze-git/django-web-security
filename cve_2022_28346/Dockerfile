FROM python:3.9

ENV PYTHONPATH /usr/src/app

WORKDIR /usr/src/app

RUN apt-get update -y
RUN apt-get install libpq-dev -y

COPY . /usr/src/app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

EXPOSE 8000
