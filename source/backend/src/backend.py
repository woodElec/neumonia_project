import sys

sys.path.append("../")
sys.path.append("../../")

import grpc

import backend_pb2_grpc
import backend_pb2

from concurrent import futures
import logging


class Backend(backend_pb2_grpc.BackendServicer):


    def load_image(self, request, context):
        patient = request.name 
        pass

    def get_prediction(self, request, context):
        pass

    def get_db_status(self, request, context):
        pass

    def save_data(self, request, context):
        pass

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