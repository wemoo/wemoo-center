from flask import Flask
from config import environment


def create_app():
    app = Flask(__name__)

    app.config.from_object(environment.config)

    from app.api import api
    app.register_blueprint(api, url_prefix='/api')

    # Init db with MongoEngine
    environment.mdb.init_app(app)

    @app.after_request
    def _after_requestresp(res):
        res.headers['Access-Control-Allow-Credentials'] = 'true'

        return res

    @app.route('/')
    def root_index():
        from common import render
        return render.ok('root index')

    return app


app = create_app()
