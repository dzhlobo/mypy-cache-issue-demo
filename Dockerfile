FROM python:3.9

RUN pip install mypy

RUN mkdir /app

WORKDIR /app
