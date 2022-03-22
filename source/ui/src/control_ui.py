from base64 import b64decode
import io
import cv2 as rq
#import backend_pb2_grpc as grpc
#import backend_pb2 as cli

def callInference(attr, old, new):
    image = io.BytesIO(b64decode(new))
    #llamar el servicio de load_image del backend y mandarle el ui_data
    #channel = grpc.insecure_channel('localhost:50051')
    #stub = cli.BackendStub(channel)
    #image_inference = stub.load_image(rq.ui_data(name, lastname,tipoId, numId,gender, image))
    print("Nombre: "+image)

def callPdf(attr, old, new):
    print("callPDF:"+new)
    
    



