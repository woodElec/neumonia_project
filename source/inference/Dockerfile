FROM python:3.8.13-slim

RUN python -m pip install --upgrade pip
RUN  apt-get update

WORKDIR /src

COPY inference/requeriments.txt requeriments.txt
COPY inference/src/inference_service.py inference_service.py
COPY protos/inference.proto inference.proto


RUN pip install -r requeriments.txt
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./inference.proto





