# -*- coding: utf-8 -*-

import simplejson

from flask import request
from common import render
from app.api import api
from app.models.task import Task


@api.route('/tasks', methods=['GET'])
def tasks_index():
    tasks = Task.objects().to_json()
    return render.ok({'tasks': tasks})


@api.route('/tasks/<string:uuid>', methods=['GET'])
def tasks_get_via_uuid(uuid):
    tasks = Task.objects(uuid=uuid).to_json()
    return render.ok({'tasks': tasks})


@api.route('/tasks', methods=['PATCH'])
def tasks_post():
    data = simplejson.loads(request.data)
    print(data)

    return render.ok()
