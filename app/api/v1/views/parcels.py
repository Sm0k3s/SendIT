"""Resources for the parcel views"""
from flask_restful import Resource, reqparse
from ..models.parcel import Parcel


class ParcelOrder(Resource):
    """
    Resource for Parcel orders /api/v1/parcels
    """
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

    def get(self):
        """Gets all parcels from the database"""
        res = Parcel.get_all()
        return {'message': 'successfully fetched', 'parcels': res}, 200

    def post(self):
        """Creates a parcel order"""
        data = ParcelOrder.parser.parse_args()
        title = data['title'].strip()
        description = data['description']
        destination = data['destination'].strip()
        pickup = data['pickup_location'].strip()
        weight = data['weight']
        if not title.isalpha():
            return {'message':'invalid title'}
        if destination == "" or pickup == "" or weight == "" or title == '':
            return {'message': 'one or more fields empty'}

        Parcel(title,destination, pickup, weight, description).create_parcel()
        i = Parcel.search_by_key_value('id', len(Parcel.database))
        return {'message': 'parcel created successfully', 'data': i}, 201


class ParcelCancel(Resource):
    """
    Resource for cancel orders /api/v1/parcels/<int:parcel_id>/cancel
    """

    def put(self, parcel_id):
        """cancels an order"""
        if parcel_id in Parcel.database.keys():
            Parcel.cancel_parcel(parcel_id)
            i = Parcel.search_by_key_value('id', parcel_id)[0]
            return {'message': 'status changed', 'data': i}, 201
        return {'message': 'parcel not found'}, 404

class FindParcel(Resource):
    """
    Resource to get a single order by id /api/v1/parcels/<int:parcel_id>
    """
    parser = reqparse.RequestParser()
    parser.add_argument('destination',
                        type=str,
                        required=True,
                        help="You must provide a new destination."
                       )

    def get(self, parcel_id):
        """Gets a single order that matches the id provided"""
        if parcel_id in Parcel.database.keys():
            i = Parcel.search_by_key_value('id', parcel_id)[0]
            return {'message': 'successfully fetched', 'data': i}, 200
        return {'message': 'parcel not found'}, 404

    def put(self,parcel_id):
        """modifies a parcels destination"""
        data = FindParcel.parser.parse_args()
        if parcel_id in Parcel.database.keys():
            Parcel.change_the_destination(parcel_id, data['destination'])
            i = Parcel.search_by_key_value('id', parcel_id)[0]
            return {'message':'parcel updated successfully','data':i}, 201
        return {'message': 'parcel not found'}, 404
