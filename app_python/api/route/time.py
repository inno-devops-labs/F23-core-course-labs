from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.schema.time import TimeSchema
from api.model.time import Time

time_blueprint = Blueprint('time', __name__)


@time_blueprint.route('/', methods=['GET'])
@swag_from({
    'responses': {
        HTTPStatus.OK.value: {
            'description': 'Current Moscow time',
            'example': TimeSchema().dump(Time())
        }
    }
})
def current_time():
    """
    Return current MSK time
    Return current MSK time with it's timezone
    ---
    """
    result = Time()
    increment()
    return TimeSchema().dump(result), 200


def increment():
    with open('/app/visits/visits', 'rw') as f:
        s = f.read()
        res = 0
        if s != '':
            res = int(s)
        f.write(str(res + 1))
