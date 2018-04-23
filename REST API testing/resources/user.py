from flask_restful import Resource, reqparse
from models.user import UserModel

"""
This is to create a new user resource.
Get the username and password and save it in the model
"""

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="TRequired")
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="Required")

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201