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
                        type=str,
                        required=True,
                        help="weight must be a digit."
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
        user = UserModel.find_by_id(get_jwt_identity())
        if not user:
            return {'message':'cannot create parcel without registering first'}, 401
        if not title.isalpha():
            return {'message':'title should only have alphabets'}, 400
        if len(destination) < 3:
            return {'message':'the destination must be atleast 3 characters long'}, 400
        if len(pickup) < 3:
            return {'message':'the pickup_location must be atleast 3 characters long'}, 400
        if len(title) < 3:
            return {'message':'the title must be atleast 3 characters long'}, 400
        if destination.isdigit():
            return {'message':'the destination should not be digits only'},400
        if not weight.isdigit():
            return {'message':'weight must be a digit'}, 400
        if int(weight) < 1:
            return {'message':'the minimum weight is 1'}, 400
        deliver = ParcelModel(title,description, destination,pickup,weight,
                              get_jwt_identity())
        deliver.save_to_db()
        return {'message':'parcel created successfully'}, 201


class CancelParcel(Resource):
    """Resource for cancelling a parcel api/v2/parcels/<parcel id>/cancel"""
    @jwt_required
    def put(self, parcel_id):
        parcel = ParcelModel.find_by_id(parcel_id)
        if not parcel:
            return {'message':'parcel does not exist'}, 404
        if parcel['sender_id'] == get_jwt_identity():
            ParcelModel.cancel_a_parcel(parcel_id)
            return {'message':'parcel {} canceled'.format(parcel_id)}, 200
        return {'message':'cannot cancel parcel thats not yours'}, 401


class EditParcel(Resource):
    """Resource for editting a parcel's destination /api/v2/parcels/<parcel id>/destination"""
    parser = reqparse.RequestParser()
    parser.add_argument('new destination',
                        type=str,
                        required=True,
                        help="You must provide a new destination."
                       )

    @jwt_required
    def put(self, parcel_id):
        data = EditParcel.parser.parse_args()
        if len(data['new destination'].strip()) < 3:
            return {'message':'destination should be atleast 3 characters long'}, 400
        if data['new destination'].isdigit():
            return {'message':'destination should not be digits only'}, 400

        parcel = ParcelModel.find_by_id(parcel_id)
        if parcel['sender_id'] != get_jwt_identity():
            return {'message': 'cannot edit a parcel that you did not create'}, 401
        ParcelModel.edit_a_parcel(data['new destination'], parcel_id)
        return {'message':'destination for parcel {} updated'.format(parcel_id)}, 200
