from flask import request,jsonify,Response
import json
import logging
from pathlib import Path
import os
import jwt
from jwt import exceptions as exc
from model.ip_tor import Ips
from model.crypto_data import CryptoData

fl = str(Path().absolute()) + "/plant.log"
print(fl)
logging.basicConfig(filename=fl, format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger() 
logger.setLevel(logging.INFO)

class Ip_Client:

    def get_ips_(self):
        try:
            authorization = request.headers['Authorization']
            crypto_data = CryptoData()
            token = crypto_data.split_authorization(authorization)
            secret = os.getenv("secret")
            version = os.getenv("version")
            token_decode = jwt.decode(token,secret,algorithms="HS256")
            if(token_decode['version'] == version ):
                ips = Ips()
                info = ips.get_ips()
                return Response(response=json.dumps(info),status=200,mimetype='application/json;charset=UTF-8')
            _response = {"msg":"FORBIDDEN"}
            return Response(response=json.dumps(_response),status=403,mimetype='application/json;charset=UTF-8')
        except (KeyError,exc.InvalidSignatureError):
            _response = {"msg":"FORBIDDEN"}
            return Response(response=json.dumps(_response),status=403,mimetype='application/json;charset=UTF-8')
        except (exc.ExpiredSignatureError):
            _response = {"msg":"EXPIRED"}
            return Response(response=json.dumps(_response),status=410,mimetype='application/json;charset=UTF-8')

    def blacklist_ip(self):
        try:
            authorization = request.headers['Authorization']
            crypto_data = CryptoData()
            token = crypto_data.split_authorization(authorization)
            secret = os.getenv("secret")
            version = os.getenv("version")
            token_decode = jwt.decode(token,secret,algorithms="HS256")
            if(token_decode['version'] == version ):
                json_data = request.get_json()
                ip = json_data['ip']
                ips = Ips()
                info = ips.blacklist_ip(ip)
                if(info == 'FAILED'):
                    _response = {
                        "msg": 'No se pudo definir la ip a borrar'
                    }
                    return Response(response=json.dumps(_response),status=400,mimetype='application/json;charset=UTF-8')
                _response = {
                    "msg": 'Ip en lista Negra'
                }
                return Response(response=json.dumps(_response),status=400,mimetype='application/json;charset=UTF-8')
            _response = {"msg":"FORBIDDEN"}
            return Response(response=json.dumps(_response),status=403,mimetype='application/json;charset=UTF-8')
        except (KeyError,exc.InvalidSignatureError):
            _response = {"msg":"FORBIDDEN"}
            return Response(response=json.dumps(_response),status=403,mimetype='application/json;charset=UTF-8')
        except (exc.ExpiredSignatureError):
            _response = {"msg":"EXPIRED"}
            return Response(response=json.dumps(_response),status=410,mimetype='application/json;charset=UTF-8')
        
            
