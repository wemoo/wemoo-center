# coding: utf8

import datetime

from config import environment

db = environment.mdb


class Task(db.Document):

    title = db.StringField(required=True, max_length=100)
    uuid = db.StringField(max_length=100)
    desc = db.StringField(required=True, max_length=1000)
    script = db.StringField(required=True)
    result = db.StringField(required=True)
    finished = db.BooleanField(default=False)

    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)
