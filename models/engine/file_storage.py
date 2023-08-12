#!/usr/bin/python3
# file_storage.py
"""Represents a file sotrage class"""
import json
from models.base_model import BaseModel


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
        """Deserializes the JSON file to __objects if it exists"""
        try:
            with open(type(self).__file_path, "r") as file:
                saved_objs = json.load(file)
                for obj in saved_objs:
                    # converts a dict to an object
                    baseModel = BaseModel(**obj)
                    obj_key = '{}.{}'.format(
                        baseModel.__class__.__name__, baseModel.id)
                    type(self).__objects[obj_key] = baseModel
        except Exception:
            pass
