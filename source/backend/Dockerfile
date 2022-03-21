FROM python:3.9.11

RUN apt-get update

WORKDIR /src

RUN echo "COPIANDO ARCHIVOS AL CONTENEDOR"
COPY backend/requirements.txt requirements.txt
COPY backend/src/backend.py backend.py
COPY protos/backend.proto backend.proto
COPY protos/inference.proto inference.proto
COPY protos/db_access.proto db_access.proto

RUN echo "INSTALANDO LIBRERIAS"
RUN pip install -r requirements.txt
RUN echo "LIBRERIAS INSTALADAS"

RUN python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. backend.proto
CMD backend.py
