from flask import Blueprint

api = Blueprint('api', __name__)

from . import logs    # NOQA
from . import tasks    # NOQA
from . import hosts    # NOQA
from . import webhook    # NOQA

__all__ = [logs, tasks, hosts, webhook]
