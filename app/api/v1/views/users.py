from flask_restful import Resource, reqparse
import re
from ..models.user import User


class SignUp(Resource):
    """
    Resource for signing up /api/v1/auth/signup
    re.match(r"[\w\d]{3,}@[\w]+\.[\w]{2,}", 'one@ff.sd')
    """
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
        i = User(data['username'], data['email'],
                 data['password']).create_user()

        return {'message': 'account successfully registered', 'user': i}, 201
        # return i
