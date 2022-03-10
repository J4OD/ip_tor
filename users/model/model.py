from typing_extensions import Required
from database.db import db
import datetime

class Users(db.Document):
    nombre = db.StringField(required=True)
    pwd = db.StringField(requied=True)
    created_at = db.DateTime(required=True)

