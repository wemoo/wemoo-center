# coding: utf8

import datetime

from config import environment

db = environment.mdb


class Task(db.Document):
    TYPE_ONCE = 1
    TYPE_CONTINUES = 2

    title = db.StringField(required=True, max_length=100)
    task_type = db.IntField(required=True)
    desc = db.StringField(required=True, max_length=1000)
    script = db.StringField(required=True)
    result = db.StringField(default=None)
    finished = db.BooleanField(default=False)

    created_at = db.DateTimeField(default=datetime.datetime.now)
    updated_at = db.DateTimeField(default=datetime.datetime.now)

    def to_dict(self):
        return {
            'title': self.title,
            'task_type': self.task_type,
            'desc': self.desc,
            'script': self.script,
            'result': self.result,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at)
        }
