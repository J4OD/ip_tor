from urllib import response
from flask import request,jsonify, Response
import json
import logging
from pathlib import Path
import os
import jwt
from jwt import exceptions
from model.users import UsersClient

fl = str(Path().absolute()) + "/plant.log"
print(fl)
logging.basicConfig(filename=fl, format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger() 
logger.setLevel(logging.INFO)

class Users_Client:

    def post_login(self):
        try:
            json_data = request.get_json()
            user_client = UsersClient()
            resp = user_client.login(json_data)
            if(resp == 'FAILED'):
                _response = {
                    "msg": "No se pudo loggear"
                }
                return Response(response=_response,status=400,mimetype='application/json;charset=UTF-8')
            _response = {
                'token': resp
            }
            return Response(response=_response,status=200,mimetype='application/json;charset=UTF-8')
        except (KeyError):
            _response = {
                "msg":'FORBIDDEN'
            }
            return Response(response=_response,status=403,mimetype='application/json;charset=UTF-8')

    def post_create(self):
        try:
            json_data = request.get_json()
            user_client = UsersClient()
            resp = user_client.create_user(json_data)
            if(resp == 'FAILED'):
                _response = {
                    "msg": "No se pudo loggear"
                }
                return Response(response=json.dumps(_response),status=400,mimetype='application/json;charset=UTF-8')
            elif(resp == 'EXISTS'):
                _response = {
                    "msg": "¡Usuario Creado!"
                }
                return Response(response=json.dumps(_response),status=401,mimetype='application/json;charset=UTF-8')
            _response = {
                'msg': resp
            }
            return Response(response=json.dumps(_response),status=200,mimetype='application/json;charset=UTF-8')
        except (KeyError):
            _response = {
                "msg":'FORBIDDEN'
            }
            return Response(response=json.dumps(_response),status=403,mimetype='application/json;charset=UTF-8')

    def get_users(self):
        user_client = UsersClient()
        res = user_client.get_users()
        return Response(response=json.dumps(res),status=200,mimetype='application/json;charset=UTF-8')