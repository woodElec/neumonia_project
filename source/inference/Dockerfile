FROM python:3.8.13-slim

RUN python -m pip install --upgrade pip
RUN  apt-get update

WORKDIR /src

COPY requeriments.txt /requeriments.txt
COPY inference_service.py /inference_service.py
COPY protos/inference.proto /protos/inference.proto


RUN pip install -r requirements.txt
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. /protos/inference.proto

RUN inference_service.py



