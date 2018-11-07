# from flask import Flask
# from flask_restful import Resource, reqparse
from flask_restful import Resource, reqparse
from .models.parcel import Parcel

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
        res = Parcel.get_all()
        return {'Message': 'Success', 'All parcel orders': res}, 200

    def post(self):
        data = ParcelOrder.parser.parse_args()
        if data['destination'].strip() =="" or data['pickup_location'].strip() =="" or data['weight'] =="":
            return {'Message': 'One or more fields empty'}

        Parcel(data['destination'],data['pickup_location'],
               data['weight']).create_parcel()

        return {'Message': 'Parcel created successfully'}, 201