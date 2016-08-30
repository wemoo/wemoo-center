from flask import Blueprint
from flask_cors import CORS

api = Blueprint('api', __name__)
CORS(api)

from . import logs    # NOQA
from . import tasks    # NOQA
from . import hosts    # NOQA
from . import webhook    # NOQA

__all__ = [logs, tasks, hosts, webhook]
