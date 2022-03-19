FROM python:3.8.13-slim

RUN python -m pip install --upgrade pip
RUN apt-get update
RUN pip install fpdf

WORKDIR /src

COPY pdf_generator/requeriments.txt requeriments.txt
COPY pdf_generator/src/pdf_generator.py pdf_generator.py
COPY protos/pdf_generator.proto pdf_generator.proto

RUN pip install -r requeriments.txt
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./pdf_generator.proto
