# coding: utf8

import datetime

from config import environment

db = environment.mdb


class Host(db.Document):

    uuid = db.StringField(required=True)
    ip = db.DictField()
    hostname = db.StringField(required=True, max_length=200)

    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)
