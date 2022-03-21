import sys
import cv2
import os
import tensorflow as tf
import numpy as np


sys.path.append("../.")
sys.path.append("../../")

import grpc

import inference_pb2_grpc
import inference_pb2

from concurrent import futures
import logging

class Inference(inference_pb2_grpc.InferenceServicer):


    def run_inference(self, request, context):
        
        image_path = request.img_path
        image= cv2.imreada(image_path)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.resize(image, (100, 100), interpolation=cv2.INTER_CUBIC)

        model_cnn = tf.keras.models.load_model('WilhemNet_86.h5')

       
        prediction = np.argmax(model_cnn.predict(image))
        percentage = np.max(model_cnn.predict(image))*100
        type = ''
        if prediction == 0:
            type = 'bacteriana'
        if prediction == 1:
            type = 'normal'
        if prediction == 2:
            type = 'viral'
        
        #falta el heatmap de la imagen predicha
        pred_imagen = image

    
        return  (pred_imagen,percentage,type)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    inference_pb2_grpc.add_InferenceServicer_to_server(Inference(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()