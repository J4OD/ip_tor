import json
from resources.users import Users_Client

def initialize_routes(app):

    @app.route('/loggin',methods=['GET'])
    def post_login():
        users_client = Users_Client()
        return users_client.post_login()
    
    @app.route('/users',methods=['POST'])
    def post_create_users():
        users_client = Users_Client()
        return users_client.post_create()

    @app.route('/users',methods=['GET'])
    def post_create_users():
        users_client = Users_Client()
        return users_client.get_users()