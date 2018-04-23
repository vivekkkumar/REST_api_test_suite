from models.user import UserModel
from tests.base_test import BaseTest


class UserTest(BaseTest):
    def test_create_user(self):
        user = UserModel('test', 'test')

        self.assertEqual(user.username, 'test',
                         "The name of the user after creation does not equal the constructor argument.")
        self.assertEqual(user.password, 'test',
                         "The password of the user after creation does not equal the constructor argument.")