# coding: utf8

import datetime
import copy

from flask import json, Response
from bson.json_util import dumps

default_headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET, POST, PUT, OPTIONS, DELETE',
    'Access-Control-Allow-Credentials': 'true',
    'Content-Type': 'application/json',
    "Access-Control-Allow-Headers": "Content-Type, X-Requested-With",
}


def not_found(reason='not found'):
    return error(reason, status_code=404)


def ok(content=''):
    msg = {'success': True, 'content': content}
    res = jsonify(msg)
    return res


def error(msg=''):
    msg = {'success': False, 'msg': msg}
    res = jsonify(msg)
    return res


def jsonify(data, status_code=200):
    res = Response(dumps(data, default=default_json_format))
    res.headers = default_headers
    res.status = 200
    return res


def redirect(location):
    headers = copy.copy(default_headers)
    headers['Location'] = location
    res = Response()
    res.status = '302'
    res.headers.extend(headers)
    return res


def default_json_format(obj):
    """Default JSON serializer."""
    if isinstance(obj, datetime.datetime):
        obj = str(obj)
    if isinstance(obj, int):
        obj = str(obj)
    return obj
