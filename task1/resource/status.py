from flask import jsonify, current_app, session
from flask_restful import Resource
from os import sched_getaffinity
import psutil
import socket

from task1.util.datetime import utc_now


class StatusResource(Resource):
    def get(self):
        test = current_app.test_client()
        response = test.get('/')

        return jsonify(
            {
                'status': 'up' if response.status_code == 200 else 'down',
                'active_connections': session['active_connections'],
                'ip_address': socket.gethostbyname(socket.gethostname()),
                'memory_total': int(psutil.virtual_memory().available / 1024**2), #MB
                'cpu_total': len(sched_getaffinity(0)),
                'current_datetime': utc_now(),
            }
        )
