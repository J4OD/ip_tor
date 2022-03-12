import json
from resources.ip_tor import Ip_Client

def initialize_routes(app):

    @app.route('/ip-torproject',methods=['GET'])
    def get_ip_projects_routes():
        ip = Ip_Client()
        return ip.get_ips_torproject()

    @app.route('/ip-danme',methods=['GET'])
    def get_ip_dan_routes():
        ip = Ip_Client()
        return ip.get_ips_dan_me()