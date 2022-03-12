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
    
    def get_ips_torproject(self):
        response_api = requests.get('https://check.torproject.org/torbulkexitlist')
        content = response_api.content.decode('utf-8')
        content = re.split(r'\n+',content)
        for data in content:
            _tipo = self.detect_ip(data)
            if(_tipo != None):
                ip_blacklist = IpBlacklist.filterby(ip=data).all()
                if(len(ip_blacklist) == 0):
                    ip_whitelist = IpWhitelist(ip=data,tipo=_tipo)
                    ip_whitelist.save()

        return 'DONE'
    
    def get_ips_dan_me(self):
        response_api = requests.get('https://www.dan.me.uk/torlist/')
        content = response_api.content.decode('utf-8')
        content = re.split(r'\n+',content)
        for data in content:
            _tipo = self.detect_ip(data)
            if(_tipo != None):
                ip_blacklist = IpBlacklist.filterby(ip=data).all()
                if(len(ip_blacklist) == 0):
                    ip_whitelist = IpWhitelist(ip=data,tipo=_tipo)
                    ip_whitelist.save()
        return 'DONE'

    def scheduler_ip(self):
        self.get_ips_dan_me()
        self.get_ips_torproject()

    