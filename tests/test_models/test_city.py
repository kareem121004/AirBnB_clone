#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from models.city import City
from models.engine.file_storage import FileStorage
import os


class TestCity(unittest.TestCase):
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
        my_city = City()
        self.assertIsInstance(my_city, City)
        self.assertIsNotNone(my_city.id)
        self.assertIsNotNone(my_city.created_at)
        self.assertIsNotNone(my_city.updated_at)
        self.assertEqual(my_city.state_id, "")
        self.assertEqual(my_city.name, "")

    def test_to_dict_method(self):
        my_city = City()
        city_dict = my_city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertIn('id', city_dict)
        self.assertIn('created_at', city_dict)
        self.assertIn('updated_at', city_dict)
        self.assertIn('__class__', city_dict)
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], "")
        self.assertEqual(city_dict['name'], "")

    def test_dict_representation(self):
        my_city = City()
        my_city.state_id = "CA"
        my_city.name = "San Francisco"

        city_dict = my_city.to_dict()
        self.assertEqual(city_dict['state_id'], "CA")
        self.assertEqual(city_dict['name'], "San Francisco")

    def test_recreate_instance(self):
        my_city = City()
        my_city.state_id = "CA"
        my_city.name = "San Francisco"

        city_dict = my_city.to_dict()

        my_new_city = City(**city_dict)
        self.assertEqual(my_city.id, my_new_city.id)
        self.assertEqual(my_city.created_at, my_new_city.created_at)
        self.assertEqual(my_city.updated_at, my_new_city.updated_at)
        self.assertEqual(my_city.state_id, my_new_city.state_id)
        self.assertEqual(my_city.name, my_new_city.name)


if __name__ == '__main__':
    unittest.main()
