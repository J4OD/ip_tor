from base64 import encode
import re 
import os
import json
import datetime
import jwt
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
        crypto_data = CryptoData()
        self.pwd = crypto_data.hash(self.pwd)
        created_at = datetime.datetime.utcnow()
        users = Users.filter_by(nombre=self.nombre).all()
        if(len(users) > 0):
            return 'EXISTS'
        user = Users(nombre=self.nombre,pwd=self.pwd, created_at=created_at)
        user.save()
        return 'DONE'

    def get_users(self):
        users = json.loads(Users.objects().to_json())
        return users
    
    def login(self,json_data):
        version = os.getenv('version')
        secret = os.getenv('secret')
        self.nombre = json_data.get("nombre",None)
        self.pwf = json_data.get("pwd",None)
        user = Users.query.filter_by(nombre=self.nombre).first()
        crypto_data = CryptoData()
        self.pwd = crypto_data.hash(self.pwd)
        if(user.pwd == self.pwd):
            payload = {
                "nombre": user.nombre,
                "version": version
            }
            token = jwt.encode(payload,secret,algorithm="HS256")
            timestamp = datetime.datetime.utcnow()
            user.logged_at = timestamp
            user.save()
            return token
        return 'FAILED'


