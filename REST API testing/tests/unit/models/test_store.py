from models.store import StoreModel
from tests.base_test import BaseTest

class StoreTest(BaseTest):
    # this is the only way to unit test since other functionalities of the model
    # interact with database and hence taken in integration teast.
    def test_create_stre(self):
        store = StoreModel('test')
        self.assertEqual(store.name, 'test' ,
                         "the name is not eqaul after creation")

