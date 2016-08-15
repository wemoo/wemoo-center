import simplejson

from flask import request
from common import render
from app.api import api
from app.models.log import Log


@api.route('/logs', methods=['POST'])
def get_user():
    data = simplejson.loads(request.data)
    app_id = data.get('app_id', None)
    level = data.get('level', None)
    log_type = data.get('log_type', None)
    content = data.get('content', None)
    if not (app_id and level and log_type and content):
        return render.error('missing')

    Log(app_id=app_id, level=level, log_type=log_type, content=content).save()

    return render.ok()
