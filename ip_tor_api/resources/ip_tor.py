from flask import request,jsonify,Response
import json
import logging
from pathlib import Path
import os
import jwt
from model.ip_tor import Ips

fl = str(Path().absolute()) + "/plant.log"
print(fl)
logging.basicConfig(filename=fl, format='%(asctime)s %(message)s',filemode='w')
logger = logging.getLogger() 
logger.setLevel(logging.INFO)

class Ip_Client:

    def get_ips_torproject(self):
        ips = Ips()
        info = ips.get_ips_torproject()
        _response = {
            "msg": info
        }
        return Response(response=json.dumps(_response),status=200,mimetype='application/json;charset=UTF-8')

    def get_ips_dan_me(self):
        ips = Ips()
        info = ips.get_ips_dan_me()
        _response = {
            "msg": 'DONE'
        }
        return Response(response=json.dumps(_response),status=200,mimetype='application/json;charset=UTF-8')
