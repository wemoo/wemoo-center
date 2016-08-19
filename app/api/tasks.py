import datetime

from flask import request
from bson.json_util import dumps
from bson.json_util import loads

from common import render
from app.api import api
from app.models.task import Task


@api.route('/tasks', methods=['GET'])
def tasks_index():
    res = {'tasks': Task.objects(), 'time': datetime.datetime.now()}
    return render.ok(res)


@api.route('/tasks/<string:uuid>', methods=['GET'])
def tasks_get_via_uuid(uuid):
    tasks = Task.objects(uuid=uuid).to_json()
    return render.ok({'tasks': tasks})


@api.route('/tasks', methods=['PATCH'])
def tasks_post():
    data = loads(request.data)
    task = Task.objects(uuid=uuid)
    print(data)

    return render.ok()
