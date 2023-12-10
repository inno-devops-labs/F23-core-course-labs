from datetime import datetime
# pylint: disable=no-name-in-module
from pydantic import BaseModel


class Visits(BaseModel):
    '''Response model for /visits/get'''
    count: int
