FROM python:3.13 as builder

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /app/

EXPOSE 8000

RUN pip install uv
RUN python -m uv sync