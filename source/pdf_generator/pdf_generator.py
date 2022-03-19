#pip install reportlab

import sys
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

sys.path.append("../.")
sys.path.append("../../")

import grpc

import pdf_generator_pb2_grpc
import pdf_generator_pb2

from concurrent import futures
import logging

class Pdf_generator(pdf_generator_pb2_grpc.Pdf_generatorServicer):


    def create_pdf(self, request, context):
        
        Nombre = request.name
        Apellido = request.id

        c = canvas.Canvas("Reporte.pdf", pagesize=A4)
        
        s = c.save()

        if s is None: #Si no se genera un objeto s no guarda
            return pdf_generator_pb2.back_response(message = 'No fue posible guardar el documento')
        else: 
            return pdf_generator_pb2.back_response(message = 'Documento guardado')

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pdf_generator_pb2_grpc.add_Pdf_generatorServicer_to_server(Pdf_generator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
