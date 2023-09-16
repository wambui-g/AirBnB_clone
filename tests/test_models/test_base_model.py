#!/usr/bin/python3
"""Test for the BaseModel class"""

from datetime import datetime
import json
import unittest
from models.base_model import BaseModel
from uuid import UUID


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel"""

    def __init__(self, *args, **kwargs):
        """ test constructor """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Set up test methods"""
        self.base = BaseModel()

    def test_id(self):
        """Tests the id"""
        self.assertTrue(hasattr(self.base, "id"))
        self.assertIsInstance(self.base.id, str)
        self.assertNotEqual(self.base.id, "")
        self.assertEqual(type(UUID(self.base.id)), UUID)

    def test_created_at(self):
        """Tests created_at"""
        self.assertTrue(hasattr(self.base, "created_at"))
        self.assertIsInstance(self.base.created_at, datetime)

    def test_updated_at(self):
        """Tests updated_at"""
        self.assertTrue(hasattr(self.base, "updated_at"))
        self.assertIsInstance(self.base.updated_at, datetime)

    def test_str(self):
        """Tests __str__"""
        self.assertEqual(str(self.base),
                         "[{}] ({}) {}".format(
            self.base.__class__.__name__, self.base.id, self.base.__dict__))

    def test_save(self):
        """Tests save"""
        self.name = 'BaseModel'
        self.value = BaseModel
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r', encoding='utf-8') as file:
            j = json.load(file)
            self.assertEqual(j[key], i.to_dict())

    def test_to_dict(self):
        """Tests to_dict"""
        self.base.name = "Name"
        self.base.my_number = 89
        self.base_json = self.base.to_dict()
        self.assertEqual(self.base_json["id"], self.base.id)
        self.assertEqual(self.base_json["__class__"],
                         self.base.__class__.__name__)
        self.assertEqual(self.base_json["created_at"],
                         self.base.created_at.isoformat())
        self.assertEqual(self.base_json["updated_at"],
                         self.base.updated_at.isoformat())
        self.assertEqual(self.base_json["name"], self.base.name)
        self.assertEqual(self.base_json["my_number"], self.base.my_number)
        self.assertEqual(type(self.base_json["created_at"]), str)
        self.assertEqual(type(self.base_json["updated_at"]), str)

    def test_kwargs(self):
        """Tests kwargs"""
        self.base.name = "Person"
        self.base.my_number = 89
        self.base_json = self.base.to_dict()
        base_new = BaseModel(**self.base_json)
        self.assertEqual(self.base.id, base_new.id)
        self.assertEqual(self.base.created_at, base_new.created_at)
        self.assertEqual(self.base.updated_at, base_new.updated_at)
        self.assertEqual(self.base.name, base_new.name)
        self.assertEqual(self.base.my_number, base_new.my_number)
        self.assertIsNot(self.base, base_new)
        self.assertIsInstance(base_new.created_at, datetime)
        self.assertIsInstance(base_new.updated_at, datetime)

    def test_kwargs_empty(self):
        """Test empty kwargs"""
        base = BaseModel()
        base.name = "Name"
        base.my_number = 89
        base_json = base.to_dict()
        base2 = BaseModel(**base_json)
        self.assertEqual(base.id, base2.id)
        self.assertEqual(base.created_at, base2.created_at)
        self.assertEqual(base.updated_at, base2.updated_at)
        self.assertEqual(base.name, base2.name)
        self.assertEqual(base.my_number, base2.my_number)
        self.assertIsNot(base, base2)
        self.assertIsInstance(base2.created_at, datetime)
        self.assertIsInstance(base2.updated_at, datetime)
