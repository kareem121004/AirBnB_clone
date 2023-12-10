#!/usr/bin/python3

import unittest
import os
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    def setUp(self):
        """Set up test environment"""
        self.file_path = "test_file.json"
        self.storage = FileStorage()
        self.obj1 = BaseModel()
        self.obj2 = User()
        self.obj3 = Place()
        self.obj4 = State()
        self.obj5 = City()
        self.obj6 = Amenity()
        self.obj7 = Review()
        self.storage.new(self.obj1)
        self.storage.new(self.obj2)
        self.storage.new(self.obj3)
        self.storage.new(self.obj4)
        self.storage.new(self.obj5)
        self.storage.new(self.obj6)
        self.storage.new(self.obj7)

    def tearDown(self):
        """Clean up test environment"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_all(self):
        """Test the all method of FileStorage"""
        objects = self.storage.all()
        self.assertEqual(type(objects), dict)
        self.assertIn(self.obj1, objects.values())
        self.assertIn(self.obj2, objects.values())
        self.assertIn(self.obj3, objects.values())
        self.assertIn(self.obj4, objects.values())
        self.assertIn(self.obj5, objects.values())
        self.assertIn(self.obj6, objects.values())
        self.assertIn(self.obj7, objects.values())

    def test_new(self):
        """Test the new method of FileStorage"""
        new_obj = BaseModel()
        self.storage.new(new_obj)
        objects = self.storage.all()
        self.assertIn(new_obj, objects.values())

    def test_save_reload(self):
        """Test the save and reload methods of FileStorage"""
        self.storage.save()
        self.storage.reload()
        objects_after_reload = self.storage.all()
        self.assertIn(self.obj1, objects_after_reload.values())
        self.assertIn(self.obj2, objects_after_reload.values())
        self.assertIn(self.obj3, objects_after_reload.values())
        self.assertIn(self.obj4, objects_after_reload.values())
        self.assertIn(self.obj5, objects_after_reload.values())
        self.assertIn(self.obj6, objects_after_reload.values())
        self.assertIn(self.obj7, objects_after_reload.values())


if __name__ == '__main__':
    unittest.main()
