from email import message
import sys
from unicodedata import name

sys.path.append("./")

import grpc

import psycopg2

import db_access_pb2_grpc
import db_access_pb2

from concurrent import futures
import logging


class DBAccess(db_access_pb2_grpc.DBAccessServicer):


    def store_patient(self, request, context):

        name = request.name
        last_name = request.last_name
        id_type = request.id_type
        id_num = request.id_num
        gender = request.gender
        img_path = request.img_path
        pred_imagen = request.pred_imagen
        percentage = request.percentage
        type = request.type

        conexion1 = psycopg2.connect(database="neumonia", user="postgres", password="admin", host="192.168.100.11")
        cursor1 = conexion1.cursor()
        sql = 'INSERT INTO "PACIENTES" (str_nombres, str_apellidos, str_tipo_documento, str_identificacion, str_genero)values (%s,%s,%s,%s,%s)'
        datos = (name, last_name, id_type, id_num, gender)
        cursor1.execute(sql, datos)
        cursor1.execute('SELECT MAX(id) id FROM "PACIENTES"')
        paciente_id = cursor1.fetchone()[0]

        sql = 'INSERT INTO "DETECCIONES" (paciente_id, num_probabilidad, str_tipo_bacteria)  values (%s,%s,%s)'
        datos = (paciente_id, percentage, type)
        cursor1.execute(sql, datos)
        cursor1.execute('SELECT MAX(id) id FROM "DETECCIONES"')
        deteccion_id = cursor1.fetchone()[0]

        sql = 'INSERT INTO "IMAGENES" (str_nombre, str_extension, str_path, num_tamano) VALUES(%s, %s, %s, %s)'
        datos = ('IMG_ORIGINAL', 'JPEG',img_path,0)
        cursor1.execute(sql, datos)
        cursor1.execute('SELECT MAX(id) id FROM "IMAGENES"')
        imagen_id = cursor1.fetchone()[0]

        sql = 'INSERT INTO "IMAGENES" (str_nombre, str_extension, str_path, num_tamano) VALUES(%s, %s, %s, %s)'
        datos = ('IMG_PREDICCION', 'JPEG',pred_imagen,0)
        cursor1.execute(sql, datos)
        cursor1.execute('SELECT MAX(id) id FROM "IMAGENES"')
        prediccion_id = cursor1.fetchone()[0]

        sql = 'INSERT INTO "DET_IMG" (deteccion_id, imagen_id, prediccion_id) values (%s,%s,%s)'
        datos = (deteccion_id, imagen_id, prediccion_id)
        cursor1.execute(sql, datos)

        conexion1.commit()
        conexion1.close()

        return db_access_pb2.store_status(message="OK")

    def load_patient(self, request, context):
        id_num = request.id_num
        respuesta = {}
        conexion1 = psycopg2.connect(database="neumonia", user="postgres", password="admin", host="192.168.100.11")
        cursor1=conexion1.cursor()
        sql=('select A.str_nombres ,A.str_apellidos,A.str_tipo_documento ,A.str_identificacion,A.str_genero,'+
        'D.str_path img_path ,E.str_path pred_imagen,B.num_probabilidad,B.str_tipo_bacteria from "PACIENTES" A '+
        'inner join "DETECCIONES" B on A.id =B.paciente_id '+
        'inner join "DET_IMG" C on B.id = C.deteccion_id inner join "IMAGENES" D on D.id =C.imagen_id '+
        'inner join "IMAGENES" E on E.id =C.prediccion_id where A.str_identificacion=\''+id_num+'\'')

        cursor1.execute(sql)
        for fila in cursor1:
            respuesta =  db_access_pb2.patient_data(
            name = fila[0],
            last_name = fila[1],
            id_type = fila[2],
            id_num = fila[3],
            gender = fila[4],
            img_path = fila[5],
            pred_imagen = fila[6],
            percentage = fila[7],
            type =  fila[8]
            )
        conexion1.close()
        return respuesta






def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_access_pb2_grpc.add_DBAccessServicer_to_server(DBAccess(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
