import sys

sys.path.append("../")
sys.path.append("../../")

import grpc
import os.path
import backend_pb2_grpc
import backend_pb2

from concurrent import futures
import logging


class Backend(backend_pb2_grpc.BackendServicer):


    def load_image(self, request, context):
        image_path = request.image_path 

        if os.path.isfile(image_path):
            print ("La ruta de la imagen es valida")
            return image_path
        else:
            print ("Por favor cargue un archivo valido")
        

    def get_prediction(self, request, context):
        pred_image = request.pred_image
    
        if os.path.exists(pred_image):
            print ("La predicción está lista")
            return pred_image
        else:
            print ("Esperando por la prediccion en inferencia")

    def get_db_status(self, request, context):
        
        # Obtenemos los datos del paciente
        image_path = request.image_path
        pred_image = request.pred_image
        name = request.name
        last_name = request.last_name
        id_type = request.id_type
        id_num = request.id_num
        gender = request.gender
                
        if os.path.isfile(image_path):
            print("Imagen cargada con exito")
            return image_path
        else:
            print("La imagen no es valida")
        
        if os.path.isfile(image_path):
            print("Predicción cargada con exito")
            return image_path
        else:
            print("La prediccion no puede ser hecha")

        if name and last_name and gender is str():
            print("Archivos cargados con exito")
            return name, last_name, gender
        else:
            print("Los archivos no son de tipo texto")
        
        if id_num and id_type is int():
            print("Archivos cargados con exito")
            return id_num, id_type
        else:
            print("Los archivos no son de tipo numerico")


    def save_data(self, request, context):
        # Obtenemos los datos del paciente
        image_path = request.image_path
        pred_image = request.pred_image
        name = request.name
        last_name = request.last_name
        id_type = request.id_type
        id_num = request.id_num
        gender = request.gender
                
        if os.path.isfile(image_path):
            print("Imagen cargada con exito")
            return image_path
        else:
            print("La imagen no es valida")
        
        if os.path.isfile(image_path):
            print("Predicción cargada con exito")
            return image_path
        else:
            print("La prediccion no puede ser hecha")

        if name and last_name and gender is str():
            print("Archivos cargados con exito")
            return name, last_name, gender
        else:
            print("Los archivos no son de tipo texto")
        
        if id_num and id_type is int():
            print("Archivos cargados con exito")
            return id_num, id_type
        else:
            print("Los archivos no son de tipo numerico")

    def create_pdf(self, request, context):

        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    backend_pb2_grpc.add_BackendServicer_to_server(Backend(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()