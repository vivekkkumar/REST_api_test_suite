from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    '''
    Gets called when user calls the /auth endpoint with their usrname and passwd
    :param username: username
    :param password: password
    :return: If passed returns UsaerModel object, None otherwise.
    '''
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    '''
    Function is called when user is verified and Flask-JWT verified the authorization header is correct
    :param payload: A dictionary with 'identity' key, user ID
    :return: Userobject model None otherwise
    '''
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)