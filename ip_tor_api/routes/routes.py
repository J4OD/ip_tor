from resources.controller import controller  

def init_routes(app):
    #default path
    @app.route('/', methods=['GET'])
    def get_controller_route():
        c = controller()
        return c.default()

    #getInfo path
    @app.route('/getips', methods=['GET'])
    def get_IP_route():
        ct = controller()
        return ct.getIps()

