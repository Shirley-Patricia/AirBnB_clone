#!/usr/bin/python3
"""
Write a class FileStorage
"""
import json
from os.path import exists
from models.base_model import BaseModel


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
        if exists(self.__file_path):
            try:
                with open(FileStorage.__file_path, 'r') as file:
                    dict_obj = json.load(file)
                for key, value in dict_obj.items():
                    FileStorage.__objects[key] = eval(f'{value["__class__"]}(**value)')

            except Exception:
                pass
