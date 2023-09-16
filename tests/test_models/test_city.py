#!/usr/bin/python3
"""Tests the City class"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Tests the City class"""

    def test_is_subclass(self):
        """tests if City is a subclass of BaseModel"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))
        self.assertTrue(hasattr(city, "updated_at"))

    def test_init(self):
        """Tests the init method"""
        city = City()
        self.assertIs(type(city.state_id), str)
        self.assertIs(type(city.name), str)
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")
