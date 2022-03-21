import sys

sys.path.append("./")

import grpc

import db_access_pb2_grpc
import db_access_pb2

from concurrent import futures
import logging


class DBAccess(db_access_pb2_grpc.DBAccessServicer):


    def store_patient(self, request, context):
        pass

    def load_patient(self, request, context):
        pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    db_access_pb2_grpc.add_DBAccessServicer_to_server(DBAccess(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()