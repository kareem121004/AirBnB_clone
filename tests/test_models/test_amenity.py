#!/usr/bin/python3

"""Unittest module for the Amenity Class."""

import unittest
from models.amenity import Amenity
from models.engine.file_storage import FileStorage
import os


class TestAmenity(unittest.TestCase):
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
        my_amenity = Amenity()
        self.assertIsInstance(my_amenity, Amenity)
        self.assertIsNotNone(my_amenity.id)
        self.assertIsNotNone(my_amenity.created_at)
        self.assertIsNotNone(my_amenity.updated_at)
        self.assertEqual(my_amenity.name, "")

    def test_to_dict_method(self):
        my_amenity = Amenity()
        amenity_dict = my_amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertIn('id', amenity_dict)
        self.assertIn('created_at', amenity_dict)
        self.assertIn('updated_at', amenity_dict)
        self.assertIn('__class__', amenity_dict)
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], "")

    def test_dict_representation(self):
        my_amenity = Amenity()
        my_amenity.name = "WiFi"

        amenity_dict = my_amenity.to_dict()
        self.assertEqual(amenity_dict['name'], "WiFi")

    def test_recreate_instance(self):
        my_amenity = Amenity()
        my_amenity.name = "WiFi"

        amenity_dict = my_amenity.to_dict()

        my_new_amenity = Amenity(**amenity_dict)
        self.assertEqual(my_amenity.id, my_new_amenity.id)
        self.assertEqual(my_amenity.created_at, my_new_amenity.created_at)
        self.assertEqual(my_amenity.updated_at, my_new_amenity.updated_at)
        self.assertEqual(my_amenity.name, my_new_amenity.name)


if __name__ == '__main__':
    unittest.main()
