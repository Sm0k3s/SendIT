from flask import Blueprint
from flask_restful import Api
from .views.users import UserSign, UserLogin
from .views.parcels import NewParcel

v2 = Blueprint('v2', __name__, url_prefix='/api/v2')
api = Api(v2)

api.add_resource(UserSign, '/auth/signup')
api.add_resource(UserLogin, '/auth/login')
api.add_resource(NewParcel, '/parcels')
