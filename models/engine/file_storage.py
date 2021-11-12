#!/usr/bin/python3
"""
Write a class FileStorage
"""


class FileStorage:
    """
    This class serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = 
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
        FileStorage.__objects = obj.__class__.__name__.id

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        to_json = {}
        for key, value in FileStorage.__objects.items():
            to_json[key] = value.to_dict()
        with open(__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        if __file_path:
            with open(__file_path, 'r') as file:
                return json.load(file)
