import base64
import io

import grpc
from PIL import Image

import backend_pb2
import backend_pb2_grpc


class UIControl:

    def __init__(self):

        channel = grpc.insecure_channel('localhost:50051')
        self.backend_stub = backend_pb2_grpc.BackendStub(channel)

    def _decode_input_data(self, data):
        data = base64.b64decode(data)
        data_bytes = io.BytesIO(data)
        image = Image.open(data_bytes)  

        return image      

    def load_image(self, attr, old, new):

        pil_image = self._decode_input_data(new)

    def create_pdf(self, attr,old, new):
        pass
