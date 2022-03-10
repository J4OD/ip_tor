import json 

import os
import base64

class CryptoData:
    
    def __init__(self):
        self.key_encrypt = os.getenv('key_encrypt')

        
    def split_authorization(self,authorization):
        vals = authorization.split(" ")
        if(vals[1]):
            return vals[1]
        return None
    
    def encrypt(self,message):
        data = str(json.dumps(message)).encode()
        encrypt = base64.b64encode(data).decode()
        return encrypt
    
    def decrypt(self,encrypted):
        decrypt = base64.b64decode(encrypted)
        decrypt = decrypt.decode()
        return decrypt
        
        