# -*- coding: utf-8 -*-

import os
import sys

from config.db import MongoDB
from config.config import Production
from config.config import Staging
from config.config import Development
from config.config import Testing

try:
    env = os.environ['FLASK_ENV']
except KeyError as e:
    sys.exit('Please set the environment key FLASK_ENV to Production/Staging/Development/Testing')


class Environment(object):
    def __init__(self):

        global env
        if env not in ('Production', 'Staging', 'Development', 'Testing'):
            print('Invalid environment key, defaulting to Development')
            env = 'Development'

        if env == 'Production':
            self.config = Production()
        elif env == 'Staging':
            self.config = Staging()
        elif env == 'Testing':
            self.config = Testing()
        else:
            self.config = Development()

        self.mdb = MongoDB()


environment = Environment()
