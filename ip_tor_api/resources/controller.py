from flask import request,Response,jsonify
import json 
import jwt 
from jwt import exceptions as exc

class controller:
    def getIps():
        try:
            allips=""
            urls_to_get = [{
                'url': 'https://check.torproject.org/torbulkexitlist',
                'method': 'GET',
            }, {
                'url': 'https://www.dan.me.uk/torlist/',
                'method': 'GET',
            }]
            responses, errors = threaded.map(urls_to_get)

            for response in responses:
                if(response.status_code==200):

                    #Escribir código para almacenar el cache de las ips de la segunda fuente
                    
                    allips+=response.text             

            return allips, 200

        except:
            return "Error!!!", 200

    def default():
        return "getips works!!!", 200  

        

