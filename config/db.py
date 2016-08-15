# -*- coding: utf-8 -*-

# from peewee import MySQLDatabase
from peewee import SqliteDatabase
#from flask.ext.mongoengine import MongoEngine
from flask_mongoengine import MongoEngine


# class MySQLDB(MySQLDatabase):
#     pass


class SqliteDB(SqliteDatabase):
    pass


class MongoDB(MongoEngine):
    pass
