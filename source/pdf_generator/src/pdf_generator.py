import sys

sys.path.append("../.")
sys.path.append("../../")

import grpc

import pdf_generator_pb2_grpc
import pdf_generator_pb2

from concurrent import futures
from fpdf import FPDF
import logging

class Pdf_generator(pdf_generator_pb2_grpc.Pdf_generatorServicer):

    
    def create_pdf(self, request, context):
        #pass
        #print('request: ', request)
        print('name: ', request.name)
        print('id: ', request.id_num)

        pdf = FPDF(orientation = 'P', unit = 'mm', format='A4')

        pdf.add_page()
        pdf.set_font('Arial', '', 16)
        pdf.text(x = 60, y = 50, txt = 'INFORME NEUMONIA')
        pdf.text(x = 60, y = 60, txt = request.name)
        pdf.text(x = 60, y = 70, txt = request.last_name)
        pdf.text(x = 60, y = 80, txt = request.id_type)
        pdf.text(x = 60, y = 90, txt = request.id_num)
        pdf.text(x = 60, y = 100, txt = request.gender)

        imagen = request.img_path
        
        pdf.image(imagen, x = 60, y = 110, w = 30, h = 30)

        imagen_pred = request.img_path_pred
        
        pdf.image(imagen_pred, x = 100, y = 110, w = 30, h = 30)

        porcentaje = request.percentage
        porcentaje = str(porcentaje)

        pdf.text(x = 60, y = 170, txt = porcentaje)
        pdf.text(x = 60, y = 180, txt = request.type)
        
        pdf.output(request.name + request.id_num + '.pdf')

        return pdf_generator_pb2.back_response(message='Hello, %s!' % request.name)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pdf_generator_pb2_grpc.add_Pdf_generatorServicer_to_server(Pdf_generator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()