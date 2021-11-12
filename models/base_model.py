#!/usr/bin/python3
"""
Console Python, first part of the AirBnB project
"""

from datetime import datetime
from uuid import uuid4
from models import storage

f = '%Y-%m-%dT%H:%M:%S.%f'


class BaseModel:

    """
        Class that defines all common attributes/methods for other classes:
    """

    def __init__(self, *args, **kwargs):

        '''
            Instance a new model

            Args:
                args:
                kwargs:

            Returns: A dictionary of values
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key in ['created_at', 'update_at']:
                    value = datetime.strptime(value, f)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            self.created_at = datetime.now()
            storage.new(self)


    def __str__(self):
        """Returns a instance in a string representation"""

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Assign update_at with the current datetime (that means: now) when this have any change"""

        self.updated_at = datetime.now().isoformat()
        storage.save(self)

    def __setattr__(self, name, value):
        self.__dict__[name] = value

    def to_dict(self):
        """Converts a instance into a dictionary format"""

        dict_BaseModel = {}
        for key in dict_BaseModel:
            setattr(self, key, dict_BaseModel[key])
        dict_BaseModel["__class__"] = self.__class__.__name__
        dict_BaseModel["updated_at"] = self.updated_at.isoformat()
        dict_BaseModel["created_at"] = self.created_at.isoformat()
        dict_BaseModel["id"] = self.id

        return dict_BaseModel
