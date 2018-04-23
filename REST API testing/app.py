import os

from flask import Flask, jsonify
# flask extension
from flask_restful import Api
from flask_jwt import JWT, JWTError

from resources.item import Item, ItemList
from resources.store import Store, StoreList
from security import authenticate, identity
from resources.user import UserRegister


app = Flask(__name__)

# for my testing
app.config['DEBUG'] = True

# Connection point of our database.

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('sqlite:///data.db')

# more on this http://flask-sqlalchemy.pocoo.org/2.1/signals/
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)

jwt = JWT(app, authenticate, identity)  # /auth endpoint

# Let us access our APIs, creating endpoints for our resources.

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

@app.errorhandler(JWTError)
def auth_error(err):
    return jsonify({'message': 'Could not authorize. Did you include a valid Authorization header?'}), 401

if __name__ == '__main__':
    from db import db

    db.init_app(app)

    if app.config['DEBUG']:
        # Decorator allows to run this func before first request is processed, doesnt run after the first request.
        # https://networklore.com/start-task-with-flask/
        @app.before_first_request
        def create_tables():
            # SQL alchemy will create the tables from the models.
            db.create_all()

    app.run(port=5000)
