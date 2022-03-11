from database.db import db
import datetime

class Users(db.Document):
    nombre = db.StringField(required=True)
    pwd = db.StringField(requied=True)
    created_at = db.DateTimeField(required=True)
    logged_at = db.DateTimeField()

