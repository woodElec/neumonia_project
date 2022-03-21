from __future__ import print_function

import logging

import grpc
import pdf_generator_pb2_grpc
import pdf_generator_pb2

def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = pdf_generator_pb2_grpc.Pdf_generatorStub(channel)
  response = stub.create_pdf(pdf_generator_pb2.patient_data(
      name='juanc', 
      last_name = 'tobar',
      id_type = 'cedula',
      id_num = '987654321',
      gender = 'hombre',
      img_path = "D:\javierimage.png",
      img_path_pred = "D:\javierimage_rota.png",
      percentage = 90.45,
      type = 'enfermo'
      ))
  print("Greeter client received: " + response.message)

if __name__ == '__main__':
    logging.basicConfig()
    run()
