#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os

class TestBaseModel(unittest.TestCase):
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
        my_model = BaseModel()
        self.assertIsInstance(my_model, BaseModel)
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_save_method(self):
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        model_dict = my_model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')

    def test_reload_method(self):
        my_model = BaseModel()
        self.storage.save()
        self.storage.reload()
        loaded_model = models.storage.all()['BaseModel.' + my_model.id]
        self.assertEqual(my_model.id, loaded_model.id)
        self.assertEqual(my_model.created_at, loaded_model.created_at)
        self.assertEqual(my_model.updated_at, loaded_model.updated_at)

if __name__ == '__main__':
    unittest.main()
