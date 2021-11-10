#!/usr/bin/python3
"""
Console Python, first part of the AirBnB project
"""

from datetime import datetime
from uuid import uuid4


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
        self.updated_at = datetime.now().isoformat()
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()

    def __str__(self):
        """Returns a instance in a string representation"""

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Assign update_at with the current datetime (that means: now) when this have any change"""

        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """Converts a instance into a dictionary format"""

        dict_BaseModel = {}
        dict_BaseModel["__class__"] = self.__class__.__name__
        dict_BaseModel["updated_at"] = self.updated_at
        dict_BaseModel["created_at"] = self.created_at
        dict_BaseModel["id"] = self.id

        return dict_BaseModel
