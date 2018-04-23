from db import db

# creating a model for the Items.

class ItemModel(db.Model):
    # defines table name and columns.

    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    store = db.relationship('StoreModel')

    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}

    # since a class would have all the states than an instance.
    @classmethod
    def find_by_name(cls, name):
        '''
        Returns the
        :param name: Name of the item to be found
        :return: Returns the model object
        '''
        # SQL alchemy method to filter name column and finds the name
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
