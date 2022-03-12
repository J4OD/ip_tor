import json
from resources.ip_tor import Ip_Client

def initialize_routes(app):

    @app.route('/ip-tor',methods=['GET'])
    def get_ip_routes():
        ip = Ip_Client()
        return ip.get_ips_torproject()

    @app.route('/ip-tor',methods=['POST'])
    def post_ip_routes():
        ip = Ip_Client()
        return ip.get_ips_dan_me()