# coding: utf8

import datetime

from config import environment

db = environment.mdb


class Host(db.Document):

    uuid = db.StringField(required=True, unique=True)
    system = db.StringField(required=True)
    hostname = db.StringField(required=True)
    release = db.StringField(required=True)
    version = db.StringField(required=True)
    machine = db.StringField(required=True)
    processor = db.StringField(required=True)
    ip = db.DictField()

    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)
