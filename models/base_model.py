#!/usr/bin/python3
"""

"""

from datetime import datetime
from uuid import uuid4


class BaseModel:

    def __init__(self, id, created_at, updated_at):
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def __str__(self):
        """should print [<class name>] (<self.id>) <self.__dict__>"""

        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at
        with the current datetime
        """

        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance"""

        dict_BaseModel = {}
        for key, value in self.__dict__.items():
        dict_rectangle[key] = value
        dict_BaseModel["__class__"] = self.__class__.__name__
        dict_BaseModel["updated_at"] = self.updated_at
        dict_BaseModel["id"] = self.id
        dict_BaseModel["created_at"] = self.created_at

        return dict_BaseModel
