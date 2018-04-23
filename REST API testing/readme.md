# REST Api Testing

I have created a sample Bare bones Flask API for my testing.

This is built with Flask, Flask-RESTful, Flask-JWT, and Flask-SQLAlchemy.

It has 3 models, items which is an item repository, store which has store information (like an item and its value) and User information.

And the rest are test. Unit, Integration and finally system test by creating a client app and interacting with get, post methods as a real use case would be.

To run these tests, navigate to test directories and run using python -m unittest (dir or filename)