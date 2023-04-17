from datetime import datetime

from models.users import UsersModel, auth, g
from utils import CustomException, lock
from flask_restful import Resource, reqparse

#Account actions (register, update, delete)
class Accounts(Resource):

    @auth.login_required()
    def get(self, username=None):
        if not username:
            account = g.user
        else:
            account = UsersModel.get_by_username(username)
        if account:
            return {"account": account.json()}, 200
        return {"message": f"Could not find an account with username [{username}]"}, 404

    # Register user
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("is_admin", type=int, required=False, nullable=False, default=0)
        parser.add_argument("username", type=str, required=True, nullable=False)
        parser.add_argument("password", type=str, required=True, nullable=False)
        parser.add_argument("email", type=str, required=True, nullable=False)
        parser.add_argument("description", type=str, required=False, nullable=False, default="")
        data = parser.parse_args()

        with lock.lock:
            if UsersModel.get_by_username(data["username"]):
                return {"message": "An account with this username already exists!"}, 409
            if UsersModel.get_by_email(data["email"]):
                return {"message": "An account with this email already exists!"}, 409
            try:
                new_account = UsersModel(
                    data["is_admin"],
                    data["username"],
                    data["email"],
                    data["description"],
                )
                new_account.hash_password(data["password"])
                new_account.save_to_db()
            except Exception:
                return {"message": "An error occurred creating the account."}, 500
            return {"account": new_account.json()}, 201

    # Update user
    @auth.login_required()
    def put(self):
        account = g.user
        parser = reqparse.RequestParser()
        parser.add_argument("is_admin", type=int, required=False, nullable=False, default=account.is_admin)
        parser.add_argument("username", type=str, required=False, nullable=False, default=account.username)
        parser.add_argument("password", type=str, required=False, nullable=False, default=None)
        parser.add_argument("email", type=str, required=False, nullable=False, default=account.email)
        parser.add_argument("description", type=str, required=False, nullable=False, default=account.description)
        data = parser.parse_args()

        with lock.lock:
            try:
                if data["username"] != account.username:
                    if UsersModel.get_by_username(data["username"]):
                        return {"message": "An account with this username already exists!"}, 409
                    account.username = data["username"]
                if data["password"] is not None:
                    account.hash_password(data["password"])
                if data["email"] != account.email:
                    if UsersModel.get_by_email(data["email"]):
                        return {"message": "An account with this email already exists!"}, 409
                    account.email = data["email"]
                account.is_admin = data["is_admin"]
                account.description = data["description"]
                account.save_to_db()
            except Exception:
                return {"message": "An error occurred updating the account."}, 500
        return {"account": account.json()}, 200

    # Delete user
    @auth.login_required()
    def delete(self, username):
        if username is None:
            return {"message": "No username specified."}, 400
        if username != g.user.username:
            return {"message": "You can't delete someone else's account."}, 403
        account = UsersModel.get_by_username(username)
        if account is None:
            return {"message": "Could not find an account with that username."}, 404
        try:
            account.delete_from_db()
        except Exception:
            return {"message": "An error occurred deleting the account."}, 500
        return {"message": "Account deleted successfully!"}, 200