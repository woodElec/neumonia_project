from __future__ import print_function

import logging

import grpc
import db_access_pb2_grpc
import db_access_pb2


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = db_access_pb2_grpc.DBAccessStub(channel)
        response = stub.store_patient(db_access_pb2.patient_data(
            name = 'Diego',
            last_name = 'Guzman Galindez',
            id_type = 'CC',
            id_num = '1130',
            gender = 'M',
            img_path ='/FOTO_ORIGINAL.JPG',
            pred_imagen = '/FOTO_PREDICCION.JPG',
            percentage = 88.7,
            type =  'ClaseA'
            ))
        print("DB ACESS store_patient client received: " + response.message)

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = db_access_pb2_grpc.DBAccessStub(channel)
        response = stub.load_patient(db_access_pb2.patient_id(id_num =  '1130'))

        print("DB ACESS load_patient client received: " + response.name,"/",response.last_name,"/",response.percentage)


if __name__ == '__main__':
    logging.basicConfig()
    run()
