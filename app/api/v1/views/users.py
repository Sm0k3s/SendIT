"""Resources for the user views"""
from flask_restful import Resource, reqparse
import re
from ..models.user import User
from ..models.parcel import Parcel


class SignUp(Resource):
    """
    Resource for signing up /api/v1/auth/signup

    """
    #re.match(r"[\w\d]{3,}@[\w]+\.[\w]{2,}", 'one@ff.sd')
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="You must provide a username."
                       )
    parser.add_argument('email',
                        type=str,
                        required=True,
                        help="You must provide an email."
                       )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="You must provide a password."
                       )

    def post(self):
        """Registers an account"""
        data = SignUp.parser.parse_args()
        if data['username'].strip() == '' or data['password'].strip() == '' or data['email'].strip() == '':
            return {'Message': 'One or more fields empty'}

        User(data['username'], data['email'], data['password']).create_user()
        return {'message': 'account successfully registered'}, 201


class UserParcels(Resource):
    """Resource to get user parcels by id"""
    def get(self,user_id):
        i = Parcel.search_by_key_value('sender_id', user_id)
        if i:
            return {'message': 'Success', 'all parcels created by user {}'.format(user_id): i}, 200
        return {'message': 'no parcel found because the user does not exist'}, 404
