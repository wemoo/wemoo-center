#!/usr/bin/env python
# coding: utf-8

import app

from flask.ext.script import Manager
from config import environment

application = app.app
manager = Manager(application)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests', pattern="*_test.py")
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def init_db():
    global application
    app.init_db(application)


@manager.command
def erase_db():
    if not environment.config.DB_ERASABLE:
        raise Exception("ERROR: It is not allowd to ERASE DB in this environment.")

    global application
    app.erase_db(application)


@manager.command
def seed():
    if not environment.config.DB_ERASABLE:
        raise Exception("This environment is not allow to add seeds to DB .")

    app.add_seed_to_db()


if __name__ == "__main__":
    manager.run()
