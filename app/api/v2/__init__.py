from flask import Blueprint
from flask_restful import Api

# from .views.parcels import ParcelOrder, ParcelCancel, FindParcel
from .views.users import UserSign#, UserParcels, UserSignin, UserSignout

v2 = Blueprint('v2', __name__, url_prefix='/api/v2')
api = Api(v2)

api.add_resource(UserSign, '/auth/signup')
