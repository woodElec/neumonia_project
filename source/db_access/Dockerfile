FROM python:3.8.3-slim

EXPOSE 50051

WORKDIR /app

COPY ./source/protos/db_access.proto db_access.proto
COPY ./source/db_access/db_access.py db_access.py
COPY ./source/db_access/client_db_access.py client_db_access.py

RUN python -m pip install --upgrade pip
RUN python -m pip install grpcio
RUN python -m pip install grpcio-tools
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./db_access.proto
RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2

CMD python db_access.py
