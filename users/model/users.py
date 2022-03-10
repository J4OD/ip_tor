import re 
import json
from .model import Users
from .crypto_data import CryptoData

class UsersClient:

    def __init__(self):
        self.nombre = ''
        self.pwd = ''

    def create_user(self, json_data):
        self.nombre = json_data.get("nombre",None)
        self.pwd = json_data.get("pwd",None)
        if(self.nombre == None or self.pwd == None):
            return 'FAILED'
        self.nombre = re.sub("[^a-zA-Z]","",self.nombre)
        self.pwd = re.sub("[^a-zA-Z]","",self.pwd)

