#!usr/bin/python3
"""Unittest for FileStorage class"""

import os
import unittest

from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage


class TestFileStorage(unittest.TestCase):
    """Test for FileStorage class"""

    def test_all(self):
        """Test all method"""
        self.assertEqual(type(storage.all()), dict)
        obj1 = BaseModel()
        obj2 = BaseModel()
        obj3 = BaseModel()
        storage.new(obj1)
        storage.new(obj2)
        storage.new(obj3)
        key = obj1.__class__.__name__ + "." + obj1.id
        self.assertTrue(key in storage.all())
        key = obj2.__class__.__name__ + "." + obj2.id
        self.assertTrue(key in storage.all())
        key = obj3.__class__.__name__ + "." + obj3.id
        self.assertTrue(key in storage.all())

    def test_new(self):
        """Test new method"""
        base = BaseModel()
        storage.new(base)
        key = base.__class__.__name__ + "." + base.id
        self.assertEqual(storage.all()[key], base)

    def test_save(self):
        """ FileStorage save method """
        new = BaseModel()
        new.save()
        self.assertTrue(os.path.exists('file.json'))

    def test_reload(self):
        """ Storage file is successfully loaded to __objects """
        new = BaseModel()
        storage.save()
        storage.reload()
        for obj in storage.all().values():
            loaded = obj
        self.assertEqual(new.to_dict()['id'], loaded.to_dict()['id'])

    def test_file_path(self):
        """Test file_path attribute"""
        self.assertEqual(type(FileStorage._FileStorage__file_path), str)

    def test_objects(self):
        """Test objects attribute"""
        self.assertEqual(type(FileStorage._FileStorage__objects), dict)

    def test_file_path_value(self):
        """Test file_path attribute value"""
        self.assertEqual(FileStorage._FileStorage__file_path, "file.json")

    def test_file_path_private(self):
        """Test file_path attribute is private"""
        with self.assertRaises(AttributeError):
            print(FileStorage.__file_path)

    def test_file_storage_reload(self):
        """Test file storage reload method"""
        storage.reload()
        self.assertEqual(type(storage.all()), dict)

    def test_file_storage_save(self):
        """Test file storage save method"""
        storage.save()
        self.assertEqual(type(storage.all()), dict)
