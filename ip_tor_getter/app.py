import atexit
from model.ip_tor import Ips

from distutils.log import debug
from flask import Flask

from database.db import initialize_db
from routes.routes import initialize_routes

from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.config['MONGO_SETTINGS'] = {
    'host': os.getenv('host_mongo')
}

initialize_db(app)
initialize_routes(app)

app.run(debug=True,port=4020,host="0.0.0.0",use_reloader=False) 
