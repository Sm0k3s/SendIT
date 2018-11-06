from .views import ParcelOrder
from flask import Blueprint, Api

v1 = Blueprint('v1', __name__, url_prefix='/api/v1')
api = Api(v1)

api.add_resource(ParcelOrder, '/orders')
