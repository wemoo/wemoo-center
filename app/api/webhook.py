import simplejson

from flask import request
from common import render
from common.shell import execute
from app.api import api

script = """
#!/bin/bash

cd /opt/kangfubao
mvn clean -Dmaven.test.skip=true package
"""


@api.route('/webhook', methods=['GET', 'POST'])
def webhook():
    data = simplejson.loads(request.data)
    print(data)

    event = data.get('event')
    repo = data.get('repository')
    if not repo:
        print('>>> not a repo')
        return render.ok('not a repo')

    repo_name = repo.get('name')
    if not repo_name:
        print('>>> repo name missing')
        return render.ok('repo name missing')

    if event in ('push', 'merge_request', 'pull_request'):
        if repo_name in ('test'):
            output = str(execute(script, 300), 'utf-8')
            print(output)
            return render.ok(output)

    return render.ok()
