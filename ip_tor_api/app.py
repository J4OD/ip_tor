import atexit
from apscheduler.schedulers.background import BackgroundScheduler
from model.ip_tor import Ips

from distutils.log import debug
from flask import Flask

from database.db import initialize_db
from routes.routes import initialize_routes

from dotenv import load_dotenv
import os

try:
    load_dotenv()

    app = Flask(__name__)
    app.config['MONGO_SETTINGS'] = {
        'host': os.getenv('host_mongo')
    }

    initialize_db(app)
    initialize_routes(app)

    ips = Ips()
    sched = BackgroundScheduler()
    sched.add_job(ips.scheduler_ip,'cron',day='*',id='sched_ip',replace_existing=True)
    sched.start()

    atexit.register(lambda:sched.shutdown())

    app.run(debug=True,port=4000,host="0.0.0.0",use_reloader=False) 

except (SystemError,KeyboardInterrupt):
    sched.remove_all_jobs()
    sched.pause()
    sched.shutdown()