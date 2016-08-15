# coding: utf-8

import simplejson

from tests.base import BaseTestCase


class LogTestCase(BaseTestCase):
    def test_create_one_log(self):
        app_id = 'test-app-id'
        level = 'info'
        log_type = 'test-type'
        content = {'level1_1': 1, 'level1_2': {'leve2_1': 1}}
        data = {'app_id': app_id, 'level': level, 'log_type': log_type, 'content': content}

        url = '/api/logs'
        res = self.test.post(url, data=simplejson.dumps(data))
        assert res.status_code == 200
        assert simplejson.loads(res.data)['status'] == 'ok'

    def test_read_one_log(self):
        pass
