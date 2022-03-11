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
        ipv6 = re.match(r'^([0-9A-Fa-f]{1,4}:){7}[0-9A-Fa-f]{1,4}$',ip)
        ipv4 = re.match(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9',ip)
        if(ipv6 == None and ipv4 != None):
            return 'ipv4'
        elif(ipv6 != None and ipv4 == None):
            return 'ipv6'
        return None
    
    def get_ips_torproject(self):
        response_api = requests.get('https://check.torproject.org/torbulkexitlist')
        print(response_api.content)
    
    def get_ips_dan_me(self):
        response_api = requests.get('https://www.dan.me.uk/torlist/')
        print(response_api.content)

    