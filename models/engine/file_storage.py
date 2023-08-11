#!/usr/bin/python3
# file_storage.py
"""Represents a file sotrage class"""
import json
import os
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
        FileStorage._objects = {'{}.{}'.format(obj.__class__.__name__, obj.id): obj}

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
                new_obj = json.load(file)
                for key, val in new_obj.items():
                    obj = self.class_dict[val['__class__']](**val)
                    type(self).__objects[key] = obj
        except Exception:
            pass
