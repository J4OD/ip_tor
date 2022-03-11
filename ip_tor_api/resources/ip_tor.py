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
        ips.get_ips_torproject()
        _response = {
            "msg": "DONE"
        }
        Response(response=_response,status=200,mimetype='application/json;charset=UTF-8')
