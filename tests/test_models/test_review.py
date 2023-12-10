#!/usr/bin/python3
"""Test model for Review class"""

import unittest
from models.review import Review
from models.engine.file_storage import FileStorage
import os


class TestReview(unittest.TestCase):
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
        my_review = Review()
        self.assertIsInstance(my_review, Review)
        self.assertIsNotNone(my_review.id)
        self.assertIsNotNone(my_review.created_at)
        self.assertIsNotNone(my_review.updated_at)
        self.assertEqual(my_review.place_id, "")
        self.assertEqual(my_review.user_id, "")
        self.assertEqual(my_review.text, "")

    def test_to_dict_method(self):
        my_review = Review()
        review_dict = my_review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)
        self.assertIn('__class__', review_dict)
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], "")
        self.assertEqual(review_dict['user_id'], "")
        self.assertEqual(review_dict['text'], "")

    def test_dict_representation(self):
        my_review = Review()
        my_review.place_id = "123"
        my_review.user_id = "456"
        my_review.text = "Great place!"

        review_dict = my_review.to_dict()
        self.assertEqual(review_dict['place_id'], "123")
        self.assertEqual(review_dict['user_id'], "456")
        self.assertEqual(review_dict['text'], "Great place!")

    def test_recreate_instance(self):
        my_review = Review()
        my_review.place_id = "123"
        my_review.user_id = "456"
        my_review.text = "Great place!"

        review_dict = my_review.to_dict()

        my_new_review = Review(**review_dict)
        self.assertEqual(my_review.id, my_new_review.id)
        self.assertEqual(my_review.created_at, my_new_review.created_at)
        self.assertEqual(my_review.updated_at, my_new_review.updated_at)
        self.assertEqual(my_review.place_id, my_new_review.place_id)
        self.assertEqual(my_review.user_id, my_new_review.user_id)
        self.assertEqual(my_review.text, my_new_review.text)


if __name__ == '__main__':
    unittest.main()
