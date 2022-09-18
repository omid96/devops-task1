from task1.task1 import status_api as api
from .status import StatusResource

api.add_resource(
    StatusResource,
    '/status',
    methods=['GET'],
    endpoint='status'
)
