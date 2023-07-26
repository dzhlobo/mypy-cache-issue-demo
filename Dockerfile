FROM python:3.11

RUN pip install mypy

RUN mkdir /app

WORKDIR /app
