FROM python:3.8.13-slim

RUN python -m pip install --upgrade pip
RUN apt-get update

WORKDIR /src

COPY requeriments /requeriments
COPY pdf_generator.py /pdf_generator.py
COPY protos/pdf_generator.proto /protos/pdf_generator.proto

RUN pip install -r requeriments.txt
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pdf_generator.proto

RUN python pdf_generator.py

