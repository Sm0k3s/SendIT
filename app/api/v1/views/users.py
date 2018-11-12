"""Resources for the user views"""
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
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
            return {'message': 'Success',
                    'all parcels created by user {}'.format(user_id): i}, 200
        return {'message': 'no parcels found, invalid user'}, 404


class UserSignin(Resource):
    """Resource for signing in a user /api/v1/auth/login"""
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="You must provide a username."
                       )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="You must provide a password."
                       )
    def post(self):
        """Method to login"""
        data = UserSignin.parser.parse_args()
        if len(User.database) < 1:
            return {'message':'user not found please create an account'}
        user = User.search_by_key_value('username', data['username'])[0]
        if data['username'].strip() == '' or data['password'].strip() == '':
            return {'message':'Please enter valid details'}
        if not user:
            return {'message':'user not found'},401
        if check_password_hash(user['password'],data['password']):
            return {'message':'successfully signed in'}, 200
        return {'message':'invalid credentials'},401

class UserSignout(Resource):
    """
    Without implementing authentication the sign out assumes that the
    current user is the last user who signed up thus he is the one who will be
    signed out /api/v1/users/logout
    """
    def delete(self):
        if len(User.database) < 1:
            return {'message':'Please login'}, 401
        user = User.search_by_key_value('id', len(User.database))[0]
        return {'message':'successfully logged out', 'user': user}
