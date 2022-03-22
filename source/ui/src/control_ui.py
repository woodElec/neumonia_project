
from base64 import b64decode
import io

def callInference(img):
    image = io.BytesIO(b64decode(img))
    #llamar el servicio de load_image del backend y mandarle el ui_data
    #channel = grpc.insecure_channel('localhost:50051')
    #stub = cli.BackendStub(channel)
    #image_inference = stub.load_image(rq.ui_data(new.name, new.lastname, new.tipoId, new.numId, new.gender, image))
    print("Nombre: ")

def callPdf(attr, old, new):
    print("callPDF_name:"+new)
    
    



