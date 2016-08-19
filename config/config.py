import os

#from config.db import MySQLDB


class Config:
    # DB = MySQLDB(
    #     os.environ.get('DB_NAME'),
    #     host=os.environ.get('DB_HOST'),
    #     port=int(os.environ.get('DB_PORT')),
    #     user=os.environ.get('DB_USER'),
    #     passwd=os.environ.get('DB_PASSWD'))

    MONGODB_SETTINGS = {'db': os.environ.get('MONGO_DB'),
                        'host': os.environ.get('MONGO_HOST'),
                        'port': int(os.environ.get('MONGO_PORT'))}

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'DBzPdEV7g97Hphu4Gc3pbfqNPYpK'
    SSL_DISABLE = False

    @staticmethod
    def init_app(app):
        pass


class Development(Config):
    DEBUG = True


class Testing(Config):
    TESTING = True


class Staging(Config):
    DEBUG = True


class Production(Config):
    DEBUG = False


config = {
    'development': Development,
    'testing': Testing,
    'staging': Staging,
    'production': Production,
    'default': Development
}
