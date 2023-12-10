#!/usr/bin/python3
"""Defines unittests for user file"""

import unittest
from models.user import User
from models.engine.file_storage import FileStorage
import os


class TestUser(unittest.TestCase):
    def setUp(self):
        # Create a unique FileStorage instance for testing
        self.storage = FileStorage()
        self.storage.reload()
        models.storage = self.storage

    def tearDown(self):
        # Clean up storage after each test
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance_creation(self):
        my_user = User()
        self.assertIsInstance(my_user, User)
        self.assertIsNotNone(my_user.id)
        self.assertIsNotNone(my_user.created_at)
        self.assertIsNotNone(my_user.updated_at)
        self.assertEqual(my_user.email, "")
        self.assertEqual(my_user.password, "")
        self.assertEqual(my_user.first_name, "")
        self.assertEqual(my_user.last_name, "")

    def test_to_dict_method(self):
        my_user = User()
        user_dict = my_user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)
        self.assertIn('__class__', user_dict)
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], "")
        self.assertEqual(user_dict['password'], "")
        self.assertEqual(user_dict['first_name'], "")
        self.assertEqual(user_dict['last_name'], "")

    def test_dict_representation(self):
        my_user = User()
        my_user.email = "user@example.com"
        my_user.first_name = "John"
        my_user.last_name = "Doe"

        user_dict = my_user.to_dict()
        self.assertEqual(user_dict['email'], "user@example.com")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")

    def test_recreate_instance(self):
        my_user = User()
        my_user.email = "user@example.com"
        my_user.first_name = "John"
        my_user.last_name = "Doe"

        user_dict = my_user.to_dict()

        my_new_user = User(**user_dict)
        self.assertEqual(my_user.id, my_new_user.id)
        self.assertEqual(my_user.created_at, my_new_user.created_at)
        self.assertEqual(my_user.updated_at, my_new_user.updated_at)
        self.assertEqual(my_user.email, my_new_user.email)
        self.assertEqual(my_user.password, my_new_user.password)
        self.assertEqual(my_user.first_name, my_new_user.first_name)
        self.assertEqual(my_user.last_name, my_new_user.last_name)


if __name__ == '__main__':
    unittest.main()
