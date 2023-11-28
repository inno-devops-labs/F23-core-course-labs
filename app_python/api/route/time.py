from http import HTTPStatus
from flask import Blueprint
from flasgger import swag_from
from api.schema.time import TimeSchema
from api.model.time import Time
import os

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

filename = './visits'

def increment():
    s = ''
    create_file_if_not_exists(filename)
    with open(filename, 'r') as f:
        s = f.read()
    res = 0
    if s != '':
        res = int(s)
    with open(filename, 'w') as f:
        f.write(str(res + 1))


def create_directory_if_not_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        print(f"Directory '{directory}' already exists.")


def create_file_if_not_exists(file_path):
    directory = os.path.dirname(file_path)
    create_directory_if_not_exists(directory)

    if not os.path.exists(file_path):
        with open(file_path, 'w'):
            print(f"File '{file_path}' created.")
    else:
        print(f"File '{file_path}' already exists.")
