"""Resources for the user views"""
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
from flask_jwt_extended import (create_access_token, jwt_required,get_jwt_identity)

from ..models.user import UserModel
from ..models.parcel import ParcelModel
from app.api.utils.validators import Validators


class UserSign(Resource):
    """Resource for signin up users api/v2/auth/signup"""
    parser = reqparse.RequestParser()
    parser.add_argument('firstname',
                        type=str,
                        required=True,
                        help="You must provide a firstname."
                       )
    parser.add_argument('surname',
                        type=str,
                        required=False,
                        help="You must provide a surname."
                       )
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
        data = UserSign.parser.parse_args()
        fname = data['firstname'].strip()
        sname = data['surname'].strip()
        uname = data['username'].strip()
        if data['username'].strip() == '' or data['password'].strip() == '' or data['email'].strip() == '':
            return {'message': 'one or more fields empty'},400
        if not fname.isalpha():
            return {'message': 'firstname should be alphabets only'}, 400
        if len(fname) < 3:
            return{'message':'firstname should be atleast 3 characters long'},400
        if not sname.isalpha():
            return {'message': 'please enter a name that consists of alphabets only'}, 400
        if len(sname) < 3:
            return{'message':'surname should be atleast 3 characters long'},400
        if len(uname) < 3:
            return {'message':'username should atleast be 3 characters long'}, 400

        if not Validators.check_username(data['username']):
            return {'message': 'please enter a valid username'}, 400

        if not Validators.check_email(data['email']):
            return {'Message': 'please enter a valid email', 'info':
            'the email should have a single character before and after the \'@\' and \'.\' signs'}, 400

        if not len(data['password'].strip()) >= 6:
            return {'message': 'password must be atleast six characters long'}, 400

        if UserModel.find_by_username(data['username']):
            return {'message':'username {} already exists '.format(data['username'])}, 400
        UserModel(data['firstname'],data['surname'],data['username'],
                      data['email'],data['password']).save_to_db()
        return {'message':'user {} successfully signed up'.format(data['username'])}, 201


class UserLogin(Resource):
    """Resource for user login api/v2/auth/login"""
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
        data = UserLogin.parser.parse_args()
        if len(data['username'].strip()) < 3:
            return {'message':'please enter a name with atleast 3 characters'}, 401
        user = UserModel.find_by_username(data['username'])
        if not user:
            return {'Message':'a user with name \'{}\' does not exist'.format(data['username']),
                    'info':'please use the name you provided when signin up'}, 401
        if check_password_hash(user['password'],data['password']):
            access_token = create_access_token(identity=user['id'])
            i = {'username':user['username'], 'email':user['email']}
            return {'Message':'login successful', 'token':access_token}
        return {'message':'invalid credentials'}, 401

class UsersParcels(Resource):
    """Resource to get all parcels by a specific user api/v2/users/<user id>/parcels"""
    @jwt_required
    def get(self, sender_id):
        if sender_id != get_jwt_identity():
            return {'message':'cannot view other users parcels'}, 401
        parcels = ParcelModel.find_by_sender_id(sender_id)
        if not parcels:
            return {'message':'parcel does not exist'}, 404
        return {'message':'parcels by {}'.format(sender_id),'all parcels': parcels}
