#!/usr/bin/python3
"""Tests State class"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Tests state class"""

    def test_is_subclass(self):
        """Test if State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_init(self):
        """Tests init method"""
        state = State()
        self.assertIs(type(state.name), str)
        self.assertEqual(state.name, "")
