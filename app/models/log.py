# coding: utf8

import datetime

from config import environment

db = environment.mdb


class Log(db.Document):

    app_id = db.StringField(required=True, max_length=100)
    level = db.StringField(required=True, max_length=10)
    log_type = db.StringField(required=True, max_length=100)
    content = db.DictField(required=True)

    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)
