#!/usr/bin/python3
"""module to define basemodel class"""

import uuid
from datetime import datetime

time_format = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:
    """definition of BaseModel class"""

    def __init__(self, *args, **kwargs):
        """initialization of the class"""

        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "Updated_at":
                    setattr(self, key, datetime.strptime
                            (value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """returns string representation of class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """updates updated_at to current time"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns dictionary containing all keys and values"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.strftime(time_format)
        obj_dict['updated_at'] = self.updated_at.strftime(time_format)
        return obj_dict
