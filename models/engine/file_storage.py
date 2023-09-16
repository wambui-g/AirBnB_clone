#!/usr/bin/python3
"""module containing Filestorage class"""

import json
from os.path import exists
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

class FileStorage:
    """filestorage class definition"""
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """ returns a dictionary of classes"""

        classes = {
                "BaseModel": BaseModel, "User": User,
                "Place": Place, "City": City, "Review": Review,
                "State": State, "Amenity": Amenity
                }
        return classes

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
        return

    def reload(self):
        """deserializes the JSON file"""
        if exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                obj_dict = json.load(file)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    obj = self.classes()[class_name](**value)
                    FileStorage.__objects[key] = obj
