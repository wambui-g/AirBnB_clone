#!/usr/bin/python3
"""module containing Filestorage class"""

import json
from os.path import exists


class FileStorage:
    """filestorage class definition"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """method that returns the dictionary objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in objects the obj with key"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes objects to the JSON file"""
        obj_dict = {key: obj.to_dict() for key, obj
                    in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        """deserializes the JSON file"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name, obj_id = key.split('.')
                    cls = class_registry.get(class_name)
                    if cls:
                        obj = cls(**value)
                        FileStorage.__objects[key] = obj


storage = FileStorage()
storage.reload()
