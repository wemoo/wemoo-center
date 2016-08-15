import simplejson

from flask import request
from common import render
from app.api import api


@api.route('/webhook', methods=['POST'])
def webhook():
    data = simplejson.loads(request.data)

    event = data.get('event')
    repo = data.get('repository')
    if not repo:
        return render.error()

    repo_name = repo.get('name')
    if not repo_name:
        return render.error()

    if event in ('push', 'merge_request', 'pull_request'):
        if repo_name in ('test'):
            print('There is a event: ', event)

    return render.ok()
