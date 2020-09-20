from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from freenit.api.methodviews import ProtectedMethodView, MethodView
from freenit.schemas.paging import PageInSchema

from ..models.social import Social
from ..schemas.social import (
    SocialPageOutSchema,
    SocialSchema,
    SocialCountSchema,
)

blueprint = Blueprint('socials', 'socials')


@blueprint.route('', endpoint='list')
class SocialListAPI(MethodView):
    @blueprint.arguments(PageInSchema(), location='headers')
    @blueprint.response(SocialPageOutSchema)
    def get(self, pagination):
        """List socials"""
        query = Social.select()
        return {
            'data': query,
            'pages': 1,
            'total': query.count(),
        }

    @jwt_required
    @blueprint.arguments(SocialSchema)
    @blueprint.response(SocialSchema)
    def post(self, args):
        """Create social"""
        social = Social(**args)
        social.save()
        return social


@blueprint.route('/<int:social_id>', endpoint='detail')
class SocialAPI(ProtectedMethodView):
    @blueprint.response(SocialSchema)
    def get(self, social_id):
        """Get social details"""
        try:
            social = Social.get(id=social_id)
        except Social.DoesNotExist:
            abort(404, message='No such social')
        return social

    @blueprint.arguments(SocialSchema(partial=True))
    @blueprint.response(SocialSchema)
    def patch(self, args, social_id):
        """Edit social details"""
        try:
            social = Social.get(id=social_id)
        except Social.DoesNotExist:
            abort(404, message='No such social')
        for field in args:
            setattr(social, field, args[field])
        social.save()
        return social

    @blueprint.response(SocialSchema)
    def delete(self, social_id):
        """Delete social"""
        try:
            social = Social.get(id=social_id)
        except Social.DoesNotExist:
            abort(404, message='No such social')
        social.delete_instance()
        return social


@blueprint.route('/count', endpoint='count')
class SocialCountAPI(MethodView):
    @blueprint.response(SocialCountSchema)
    def get(self):
        """Social count"""
        return {'total': Social.select().count()}
