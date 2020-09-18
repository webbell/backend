import sys
from freenit.schemas.base import BaseSchema
from freenit.schemas.paging import PageOutSchema
from marshmallow import fields


class MedicCountSchema(BaseSchema):
    total = fields.Integer(description='Count', dump_only=True)


class MedicSchema(BaseSchema):
    id = fields.Integer(description='ID', dump_only=True)
    academic = fields.Str(description='Academic')
    city = fields.Str(description='City')
    name = fields.Str(description='Name')
    specialty = fields.Str(description='Specialty')
    title = fields.Str(description='Title')


PageOutSchema(MedicSchema, sys.modules[__name__])
