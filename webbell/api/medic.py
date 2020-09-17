from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from freenit.api.methodviews import ProtectedMethodView, MethodView
from freenit.schemas.paging import PageInSchema, paginate

from ..models.medic import Medic
from ..schemas.medic import MedicPageOutSchema, MedicSchema

blueprint = Blueprint('medics', 'medics')


@blueprint.route('', endpoint='list')
class MedicListAPI(MethodView):
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(MedicPageOutSchema)
    def get(self, pagination):
        """List medics"""
        return paginate(Medic.select(), pagination)

    @jwt_required
    @blueprint.arguments(MedicSchema)
    @blueprint.response(MedicSchema)
    def post(self, args):
        """Create medic"""
        medic = Medic(**args)
        medic.save()
        return medic


@blueprint.route('/<int:medic_id>', endpoint='detail')
class MedicAPI(ProtectedMethodView):
    @blueprint.response(MedicSchema)
    def get(self, medic_id):
        """Get medic details"""
        try:
            medic = Medic.get(id=medic_id)
        except Medic.DoesNotExist:
            abort(404, message='No such medic')
        return medic

    @blueprint.arguments(MedicSchema(partial=True))
    @blueprint.response(MedicSchema)
    def patch(self, args, medic_id):
        """Edit medic details"""
        try:
            medic = Medic.get(id=medic_id)
        except Medic.DoesNotExist:
            abort(404, message='No such medic')
        for field in args:
            setattr(medic, field, args[field])
        medic.save()
        return medic

    @blueprint.response(MedicSchema)
    def delete(self, medic_id):
        """Delete medic"""
        try:
            medic = Medic.get(id=medic_id)
        except Medic.DoesNotExist:
            abort(404, message='No such medic')
        medic.delete_instance()
        return medic
