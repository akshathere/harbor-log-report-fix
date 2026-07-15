FROM python:3.11-slim@sha256:9e885f8239c31f8429448f933638dd13037c9119e2a362aeebdd37ec3bee7c85

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log