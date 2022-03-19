import sys

sys.path.append("../.")
sys.path.append("../../")

import grpc

import pdf_generator_pb2_grpc
import pdf_generator_pb2

from concurrent import futures
import logging

class Pdf_generator(pdf_generator_pb2_grpc.Pdf_generatorServicer):


    def create_pdf(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pdf_generator_pb2_grpc.add_Pdf_generatorServicer_to_server(Pdf_generator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()