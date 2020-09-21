import sys
from freenit.schemas.base import BaseSchema
from freenit.schemas.paging import PageOutSchema
from marshmallow import fields


class SocialCountSchema(BaseSchema):
    total = fields.Integer(description='Count', dump_only=True)


class SocialSchema(BaseSchema):
    id = fields.Integer(description='ID', dump_only=True)
    specialty = fields.Str(description='Specialty')
    name = fields.Str(description='Name')


PageOutSchema(SocialSchema, sys.modules[__name__])
