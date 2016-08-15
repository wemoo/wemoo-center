# coding: utf8

import datetime

from config import environment

db = environment.mdb


class TaskOutcome(db.Document):

    task = db.ObjectIdField(required=True)
    result = db.StringField(required=True)
    success = db.BooleanField(required=True)

    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)
