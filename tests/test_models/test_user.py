#!/usr/bin/python3
"""Tests for User class"""

import datetime
import unittest

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Tests User"""
    def test_is_subclass(self):
        """Test if User is a subclass of BaseModel"""
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertTrue(hasattr(user, "id"))
        self.assertTrue(hasattr(user, "created_at"))
        self.assertTrue(hasattr(user, "updated_at"))

    def test_user(self):
        """Tests for User"""
        u = User()
        self.assertIsInstance(u, User)
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))
        self.assertEqual(u.email, "")
        self.assertEqual(u.password, "")
        self.assertEqual(u.first_name, "")
        self.assertEqual(u.last_name, "")
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))
        self.assertTrue(type(u.id), str)
        self.assertTrue(type(u.created_at), datetime.datetime)
        self.assertTrue(type(u.updated_at), datetime.datetime)
