from datetime import datetime
# pylint: disable=no-name-in-module
from pydantic import BaseModel

class NowTime(BaseModel):
    '''Response model for /time/now'''
    timestamp: datetime
