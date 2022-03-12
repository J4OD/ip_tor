import re
import os
import json

from .model import IpWhitelist
from .model import IpBlacklist
from .crypto_data import CryptoData
import requests

class Ips:

    def __init__(self):
        self.ip_json = []
        self.ip = ''
    
    def detect_ip(self,ip):
        ipv6 = re.match(r"^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$",ip)
        ipv4 = re.match(r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$",ip)
        print(ipv4,ipv6)
        if(ipv6 == None and ipv4 != None):
            return 'ipv4'
        elif(ipv6 != None and ipv4 == None):
            return 'ipv6'
        return None
    
    def get_ips(self):
        ip_whitelist = json.loads(IpWhitelist.objects().to_json())
        return ip_whitelist

    def blacklist_ip(self,ip):
        tipo = self.detect_ip(ip)
        if(tipo == 'None'):
            return 'FAILED'
        ip_whitelist = IpWhitelist.object(ip=ip)
        if(len(ip_whitelist)>0):
            ip_whitelist.first().delete()
        ip_blacklist = IpBlacklist(ip=ip,tipo=tipo)
        ip_blacklist.save()
        return 'DONE'


    