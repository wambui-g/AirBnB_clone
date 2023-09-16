#!/usr/bin/python3
"""Tests the Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Tests the Review class"""

    def test_is_subclass(self):
        """Test if Review is a subclass of BaseModel"""
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertTrue(hasattr(review, "id"))
        self.assertTrue(hasattr(review, "created_at"))
        self.assertTrue(hasattr(review, "updated_at"))

    def test_init(self):
        """Tests the init method"""
        review = Review()
        self.assertIs(type(review.place_id), str)
        self.assertIs(type(review.user_id), str)
        self.assertIs(type(review.text), str)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")
