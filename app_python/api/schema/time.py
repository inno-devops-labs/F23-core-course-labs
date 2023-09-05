from marshmallow import Schema, fields


class TimeSchema(Schema):
    time = fields.Str()
    timezone = fields.Str()
