#!/usr/bin/python3
# file_storage.py
"""Represents a file sotrage class"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage():
    """Represents a file storage class

    Attributes:
        _file_path:(String) - path to JSON file
        _objects:(dictionary) - a dictonary to store an objects with key <class name>.id and value class.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ returns the dictionary of an objects"""
        return type(self).__objects

    def new(self, obj):
        """creats a new dictionary of an object vs id pair"""
        obj_key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        # check if this object is already stored
        if self.__objects.keys().__contains__(obj_key):
            return
        type(self).__objects[obj_key] = obj

    def save(self):
        """serializes the object to JSON file"""
        new_dict = []
        for obj in type(self).__objects.values():
            new_dict.append(obj.to_dict())
        with open(type(self).__file_path, "w", encoding='utf-8') as file:
            json.dump(new_dict, file)

    def reload(self):
        """desrializes the JSON file to object only if the file path exists."""
        try:
            with open(type(self).__file_path, "r") as file:
                saved_objs = json.load(file)
                for dic in saved_objs:
                    # converts a dict to an object
                    if dic['__class__'] == 'BaseModel':
                        obj = BaseModel(**dic)
                    elif dic['__class__'] == 'User':
                        obj = User(**dic)
                    obj_key = '{}.{}'.format(
                        obj.__class__.__name__, obj.id)
                    type(self).__objects[obj_key] = obj
        except Exception:
            pass
