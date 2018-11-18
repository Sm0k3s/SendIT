from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, jwt_required,get_jwt_identity)
from ..models.user import UserModel
from ..models.parcel import ParcelModel
from app.api.utils.validators import Validators


class NewParcel(Resource):
    """Resource to create a new parcel order api/v2/parcels"""
    parser = reqparse.RequestParser()
    parser.add_argument('title',
                        type=str,
                        required=True,
                        help="You must provide title."
                       )
    parser.add_argument('description',
                        type=str,
                        required=False,
                        help="You description of parcel."
                       )
    parser.add_argument('destination',
                        type=str,
                        required=True,
                        help="You must provide a destination."
                       )
    parser.add_argument('pickup_location',
                        type=str,
                        required=True,
                        help="You must provide a pickup_location."
                       )
    parser.add_argument('weight',
                        type=int,
                        required=True,
                        help="You must provide weight."
                       )
    @jwt_required
    def post(self):
        """Creates a parcel order"""
        data = NewParcel.parser.parse_args()
        title = data['title'].strip()
        description = data['description']
        destination = data['destination'].strip()
        pickup = data['pickup_location'].strip()
        weight = data['weight']
        if not title.isalpha():
            return {'message':'invalid title'}
        if len(destination) < 3 or len(pickup) < 3 or weight < 0 or len(title) < 3:
            return {'message': 'one or more fields invalid'}
        deliver = ParcelModel(title,description, destination,pickup,weight,
                              get_jwt_identity())
        deliver.save_to_db()
        return {'message':'parcel created successfully'}, 201
