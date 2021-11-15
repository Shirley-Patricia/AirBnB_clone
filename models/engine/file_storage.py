#!/usr/bin/python3
"""
Write a class FileStorage
"""
import json
from os.path import exists
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        name = obj.__class__.__name__
        identifier = obj.id
        FileStorage.__objects[name + "." + identifier] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        to_json = {}
        for key, value in FileStorage.__objects.items():
            to_json[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(to_json, file)

    def reload(self):
        """
            deserializes __objects to the JSON file (path: __file_path)
        """
        if exists(self.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    dict_obj = json.load(file)
                for k, v in dict_obj.items():
                    self.__objects[k] = eval(f'{v["__class__"]}(**v)')

            except Exception:
                pass
