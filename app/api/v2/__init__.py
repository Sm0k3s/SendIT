from flask import Blueprint
from flask_restful import Api

# from .views.parcels import ParcelOrder, ParcelCancel, FindParcel
# from .views.users import SignUp, UserParcels, UserSignin, UserSignout

v2 = Blueprint('v1', __name__, url_prefix='/api/v2')
api = Api(v2)

# api.add_resource(ParcelOrder, '/parcels')
