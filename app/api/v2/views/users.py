"""Resources for the user views"""
from flask_restful import Resource, reqparse
from werkzeug.security import check_password_hash
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
        fname = data['firstname']
        sname = data['surname']
        if data['username'].strip() == '' or data['password'].strip() == '' or data['email'].strip() == '':
            return {'message': 'one or more fields empty'}
        if not fname.isalpha() or len(fname) < 3:
            return {'message': 'invalid firstname'}, 401
        if not sname.isalpha() or len(sname) < 3:
            return {'message': 'invalid surname'}, 401
        if not Validators.check_username(data['username']):
            return {'message': 'please enter a valid username'}, 401

        if not Validators.check_email(data['email']):
            return {'message': 'please enter a valid email'}, 401

        if not len(data['password'].strip()) >= 6:
            return {'message': 'password must be atleast six characters long'}, 401

        if not Validators.check_password(data['password']):
            return {'message': 'password should have a mixed combination'}

        if UserModel.find_by_username(data['username']):
            return {'message':'username {} already exists '.format(data['username'])}, 401
        UserModel(data['firstname'],data['surname'],data['username'],
                      data['email'],data['password']).save_to_db()
        return {'message':'user {} created'.format(data['username'])}, 201
