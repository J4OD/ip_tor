from database.db import db
import datetime

class IpWhitelist(db.Document):
    ip = db.StringField(required=True)
    tipo = db.StringField(required=True)

class IpBlacklist(db.Document):
    ip = db.StringField(required=True)
    tipo = db.StringField(required=True)
    

