FROM python:3.8.13-slim

RUN wget --no-check-certificate https://www.dropbox.com/s/6ddnsrd6jhc8my4/WilhemNet_86%20%282%29.h5?dl=0 -O WilhemNet_86.h5
RUN python -m pip install --upgrade pip
RUN  apt-get update


WORKDIR /src

COPY inference/requeriments.txt requeriments.txt
COPY inference/src/inference_service.py inference_service.py
COPY protos/inference.proto inference.proto


RUN pip install -r requeriments.txt
RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./inference.proto





