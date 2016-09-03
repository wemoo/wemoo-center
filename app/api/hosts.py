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
        host = Host.objects(uuid=data['uuid']).get(0)
        return render.ok(host.to_dict())
    else:
        return render.error()


@api.route('/hosts', methods=['GET'])
def hosts_index():
    hosts = [host for host in Host.objects()]
    host_list = []
    for host in hosts:
        host_list.append(host.to_dict())
    res = {'hosts': host_list}
    return render.ok(res)


@api.route('/hosts/<string:host_id>', methods=['GET'])
def hosts_get_by_id(host_id):
    hosts = Host.objects(id=host_id)
    if len(hosts) > 0:
        host = hosts.get(0)
        return render.ok({'host': host.to_dict()})
    else:
        return render.not_found()
