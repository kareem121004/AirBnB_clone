#!/usr/bin/python3
"""Test model for Place class"""

import unittest
from models.place import Place
from models.engine.file_storage import FileStorage
import os


class TestPlace(unittest.TestCase):
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
        my_place = Place()
        self.assertIsInstance(my_place, Place)
        self.assertIsNotNone(my_place.id)
        self.assertIsNotNone(my_place.created_at)
        self.assertIsNotNone(my_place.updated_at)
        self.assertEqual(my_place.name, "")
        self.assertEqual(my_place.city_id, "")
        self.assertEqual(my_place.user_id, "")
        self.assertEqual(my_place.description, "")
        self.assertEqual(my_place.number_rooms, 0)
        self.assertEqual(my_place.number_bathrooms, 0)
        self.assertEqual(my_place.max_guests, 0)
        self.assertEqual(my_place.price_by_night, 0)
        self.assertEqual(my_place.latitude, 0.0)
        self.assertEqual(my_place.longitude, 0.0)
        self.assertEqual(my_place.amenity_ids, [])

    def test_to_dict_method(self):
        my_place = Place()
        place_dict = my_place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertIn('id', place_dict)
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIn('__class__', place_dict)
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['name'], "")
        self.assertEqual(place_dict['city_id'], "")
        self.assertEqual(place_dict['user_id'], "")
        self.assertEqual(place_dict['description'], "")
        self.assertEqual(place_dict['number_rooms'], 0)
        self.assertEqual(place_dict['number_bathrooms'], 0)
        self.assertEqual(place_dict['max_guests'], 0)
        self.assertEqual(place_dict['price_by_night'], 0)
        self.assertEqual(place_dict['latitude'], 0.0)
        self.assertEqual(place_dict['longitude'], 0.0)
        self.assertEqual(place_dict['amenity_ids'], [])

    def test_dict_representation(self):
        my_place = Place()
        my_place.name = "Cozy Cabin"
        my_place.city_id = "SF"
        my_place.user_id = "123"
        my_place.description = "A beautiful place in the woods"
        my_place.number_rooms = 2
        my_place.number_bathrooms = 1
        my_place.max_guests = 4
        my_place.price_by_night = 100
        my_place.latitude = 37.7749
        my_place.longitude = -122.4194
        my_place.amenity_ids = ["1", "2", "3"]

        place_dict = my_place.to_dict()
        self.assertEqual(place_dict['name'], "Cozy Cabin")
        self.assertEqual(place_dict['city_id'], "SF")
        self.assertEqual(place_dict['user_id'], "123")
        self.assertEqual(
            place_dict['description'],
            "A beautiful place in the woods"
        )
        self.assertEqual(place_dict['number_rooms'], 2)
        self.assertEqual(place_dict['number_bathrooms'], 1)
        self.assertEqual(place_dict['max_guests'], 4)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 37.7749)
        self.assertEqual(place_dict['longitude'], -122.4194)
        self.assertEqual(place_dict['amenity_ids'], ["1", "2", "3"])

    def test_recreate_instance(self):
        my_place = Place()
        my_place.name = "Cozy Cabin"
        my_place.city_id = "SF"
        my_place.user_id = "123"
        my_place.description = "A beautiful place in the woods"
        my_place.number_rooms = 2
        my_place.number_bathrooms = 1
        my_place.max_guests = 4
        my_place.price_by_night = 100
        my_place.latitude = 37.7749
        my_place.longitude = -122.4194
        my_place.amenity_ids = ["1", "2", "3"]

        place_dict = my_place.to_dict()

        my_new_place = Place(**place_dict)
        self.assertEqual(my_place.id, my_new_place.id)
        self.assertEqual(my_place.created_at, my_new_place.created_at)
        self.assertEqual(my_place.updated_at, my_new_place.updated_at)
        self.assertEqual(my_place.name, my_new_place.name)
        self.assertEqual(my_place.city_id, my_new_place.city_id)
        self.assertEqual(my_place.user_id, my_new_place.user_id)
        self.assertEqual(my_place.description, my_new_place.description)
        self.assertEqual(my_place.number_rooms, my_new_place.number_rooms)
        self.assertEqual(
            my_place.number_bathrooms,
            my_new_place.number_bathrooms
        )
        self.assertEqual(my_place.max_guests, my_new_place.max_guests)
        self.assertEqual(my_place.price_by_night, my_new_place.price_by_night)
        self.assertEqual(my_place.latitude, my_new_place.latitude)
        self.assertEqual(my_place.longitude, my_new_place.longitude)
        self.assertEqual(my_place.amenity_ids, my_new_place.amenity_ids)


if __name__ == '__main__':
    unittest.main()
