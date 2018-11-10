"""Adds the Blueprint resources"""
from flask import Blueprint
from flask_restful import Api

from .views.parcels import ParcelOrder, ParcelCancel, FindParcel
from .views.users import SignUp, UserParcels

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

api.add_resource(ParcelOrder, '/parcels')
api.add_resource(ParcelCancel, '/parcels/<int:parcel_id>/cancel')
api.add_resource(FindParcel, '/parcels/<int:parcel_id>')
api.add_resource(SignUp, '/auth/signup')
api.add_resource(UserParcels, '/users/<int:user_id>/parcels')
