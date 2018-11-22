from flask_restful import Resource, reqparse
from flask_jwt_extended import (create_access_token, jwt_required,get_jwt_identity)
from ..models.user import UserModel, admin
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
        description = data['description'].strip()
        destination = data['destination'].strip()
        pickup = data['pickup_location'].strip()
        weight = data['weight']
        user = UserModel.find_by_id(get_jwt_identity())
        if not user:
            return {'message':'cannot create parcel without registering first'}, 401
        if not title.isalpha():
            return {'message':'title should only have alphabets'}, 400
        if len(destination) < 3 or len(pickup) < 3 or len(title) < 3:
            return {'message':'the title, destination and pickup_location must be\
                    atleast 3 characters long'}, 400
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
        parcel = ParcelModel.find_by_id(parcel_id)
        return {'message':'destination for parcel {} updated'.format(parcel_id),
                'parcel': parcel}, 200


class UpdateStatus(Resource):
    """Resource for admin change status of a parcel /parcels/<parcel_id>/status"""
    @jwt_required
    @admin
    def put(self, parcel_id):
        parcel = ParcelModel.find_by_id(parcel_id)
        if not parcel:
            return {'message':'parcel does not exist'}, 404
        ParcelModel.change_status(parcel_id)
        return {'message':'updated status for parcel {}'.format(parcel_id)}, 200

class UpdateCurrentLocation(Resource):
    """Resource for admin to change current location api/v2/parcels/parcel_id/presentLocation"""
    parser = reqparse.RequestParser()
    parser.add_argument('location',
                        type=str,
                        required=True,
                        help="You must provide the current location."
                       )
    @jwt_required
    @admin
    def put(self, parcel_id):
        data = UpdateCurrentLocation.parser.parse_args()
        if len(data['location'].strip()) < 3:
            return {'message':'location should be atleast 3 characters long'}, 400
        if data['location'].isdigit():
            return {'message':'current location should not be digits only'}, 400
        ParcelModel.change_current_location(data['location'], parcel_id)
        parcel = ParcelModel.find_by_id(parcel_id)
        return {'message':'parcel updated successfully', 'parcel': parcel}, 200


class AllParcels(Resource):
    """Resource to get all parcels in the app /api/v2/parcels"""
    @jwt_required
    @admin
    def get(self):
        parcels = ParcelModel.get_all_parcels()
        if parcels is None:
            return {'message':'no parcels yet, check later'}, 404
        return {'all parcels':parcels}, 200
