FROM python:3.8.12

RUN apt-get update && \
    apt-get install python3-opencv -y && \
    apt-get install python3-pip -y

WORKDIR /src
COPY ui/src/ui_control.py /src/ui_control.py
COPY ui/src/ui.py /src/ui.py

COPY ui/requirements.txt /src/requirements.txt
RUN python3.9 -m pip install -r requirements.txt

COPY protos /src/
RUN python3.9 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./backend.proto
