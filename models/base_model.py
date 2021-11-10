#!/usr/bin/python3
"""

"""

from datetime import datetime
from uuid import uuid4


class BaseModel:

    def __init__(self, *args, **kwargs):
        self.updated_at = datetime.now().isoformat()
        self.id = str(uuid4())
        self.created_at = datetime.now().isoformat()

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
        dict_BaseModel["__class__"] = self.__class__.__name__
        dict_BaseModel["updated_at"] = self.updated_at
        dict_BaseModel["created_at"] = self.created_at
        dict_BaseModel["id"] = self.id

        return dict_BaseModel
