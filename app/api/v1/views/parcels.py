"""Resources for the parcel views"""
from flask_restful import Resource, reqparse
from ..models.parcel import Parcel


class ParcelOrder(Resource):
    """
    Resource for Parcel orders /api/v1/parcels
    """
    parser = reqparse.RequestParser()
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

    def get(self):
        """Gets all parcels from the database"""
        res = Parcel.get_all()
        return {'Message': 'Success', 'All parcel orders': res}, 200

    def post(self):
        """Creates a parcel order"""
        data = ParcelOrder.parser.parse_args()
        if data['destination'].strip() == "" or data['pickup_location'].strip() == "" or data['weight'] == "":
            return {'Message': 'One or more fields empty'}

        Parcel(data['destination'], data['pickup_location'],
               data['weight']).create_parcel()

        return {'Message': 'Parcel created successfully'}, 201


class ParcelCancel(Resource):
    """
    Resource for cancel orders /api/v1/parcels/<int:parcel_id>/cancel
    """
    parser = reqparse.RequestParser()
    parser.add_argument('status',
                        type=str,
                        required=True,
                        help="You must provide a status."
                        )

    def put(self, parcel_id):
        data = ParcelCancel.parser.parse_args()

        if data['status'] == 'cancel':
            Parcel.cancel_parcel(parcel_id)
            return {'message': 'status changed'}, 201


class FindParcel(Resource):
    """
    Resource to get a single order by id /api/v1/parcels/<int:parcel_id>
    """

    def get(self, parcel_id):
        """Gets a single order that matches the id provided"""
        if parcel_id in Parcel.database.keys():
            i = Parcel.search_by_key_value('id', parcel_id)[0]
            return {'message': 'Success', 'parcel': i}, 200
        return {'message': 'Parcel not found'}, 404
