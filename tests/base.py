# encoding: utf-8

import unittest
import app

from config import environment


class BaseTestCase(unittest.TestCase):
    def setUp(self):
        # Empty log/Testing.log file.
        open('log/Testing.log', 'w').close()

        self.app = app.create_app()
        self.app.config.from_object(environment.config)

        self.test = self.app.test_client()

        # Empty DB
        db_type = environment.config.DB.__class__.__name__
        if db_type is 'MongoDB':
            environment.mdb.drop_database('analytics_test')

    def tearDown(self):
        pass
