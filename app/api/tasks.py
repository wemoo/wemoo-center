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
    tasks = [task for task in Task.objects()]
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    res = {'tasks': task_list}
    return render.ok(res)


@api.route('/tasks/<string:tid>', methods=['GET'])
def tasks_get_by_id(tid):
    tasks = Task.objects(id=tid)
    if len(tasks) > 0:
        task = tasks.get(0)
        return render.ok({'task': task.to_dict()})
    else:
        return render.not_found()


@api.route('/tasks', methods=['POST'])
def tasks_post():
    data = loads(request.data.decode('utf-8'))
    title = data.get('title', None)
    desc = data.get('desc', None)
    script = data.get('script', None)

    if title and desc and script:
        task = Task(title=title, desc=desc, task_type=Task.TYPE_SINGLE, script=script)
        task.save()
    else:
        return render.error("Params missing.")

    return render.ok(str(task.id))
