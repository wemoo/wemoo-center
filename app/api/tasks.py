import datetime
import uuid

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


@api.route('/tasks', methods=['POST'])
def tasks_post():
    print('>>>', request.data)
    return render.ok()

    data = loads(str(request.data))
    title = data.get('title', None)
    desc = data.get('desc', None)
    script = data.get('script', None)

    if title and desc and script:
        task = Task(title=title, desc=desc, script=script)
        task.save()
    else:
        return render.error("Params missing.")

    return render.ok()
