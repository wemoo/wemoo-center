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
    uuid = data.get('uuid', None)
    hostname = data.get('hostname', None)

    if not (uuid and hostname):
        return render.error()

    now = datetime.datetime.now()
    result = Host.objects(uuid=uuid).update(set__hostname=hostname,
                                            set_on_insert__created_at=now,
                                            updated_at=now,
                                            upsert=True)
    if result > 0:
        return render.ok()
    else:
        return render.error()
