#!/usr/bin/python3

"""Defines all common attributes/methods for other classes"""

import uuid
from datetime import datetime
import models


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialization of a Base instance."""

        dtime_format = '%Y-%m-%dT%H:%M:%S.%f'
        for key, value in kwargs.items():
            if key == '__class__':
                continue
            elif key == 'created_at':
                self.created_at = datetime.strptime(
                    kwargs['created_at'], dtime_format)
            elif key == 'updated_at':
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], dtime_format)
            else:
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns a readable string representation"""
        clsName = self.__class__.__name__
        return "[{}] ({}) {}".format(clsName, self.id, self.__dict__)

    def save(self):
        """Updates the datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary that contains all"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
