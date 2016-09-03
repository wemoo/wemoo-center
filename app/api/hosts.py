# -*- coding: utf-8 -*-

import datetime
import simplejson

from flask import request
from common import render
from app.api import api
from app.models.host import Host


@api.route('/hosts', methods=['POST'])
def hosts_post():
    data = simplejson.loads(request.data)

    now = datetime.datetime.now()
    result = Host.objects(uuid=data['uuid']).update(
        set__system=data['system'],
        set__hostname=data['node'],
        set__release=data['release'],
        set__version=data['version'],
        set__machine=data['machine'],
        set__processor=data['processor'],
        set_on_insert__created_at=now,
        updated_at=now,
        upsert=True)

    if result > 0:
        return render.ok()
    else:
        return render.error()
