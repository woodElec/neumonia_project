import sys

sys.path.append("../.")
sys.path.append("../../")

import grpc

import inference_pb2_grpc
import inference_pb2

from concurrent import futures
import logging

class Inference(inference_pb2_grpc.InferenceServicer):

    def run_inference(self, request, context):
        pass

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inference_pb2_grpc.add_InferenceServicer_to_server(Inference(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()