#!/usr/bin/python3
# base_model.py
"""This is a base model class from which all other classes inherits
"""
import datetime
import uuid


class BaseModel:
    """Represent the base model."""

    def __init__(self):
        """Represents the "base" for all other classes in this project
    
         Attributes:
            id(String) : a unique id given to an instance of a class.
            created_at(datetime): stores current datetime when an instance is created
            updated_at(datetime): stores the datetime when an instance is updated.

         Args:
            - *args: list of arguments
            - **kwargs: dict of key-alues arguments
    """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        """Updates the public instance attribute updated_at
        with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary that contains all
        keys/values of the instance"""
        my_dict = self.__dict__.copy()
        my_dict['updated_at'] = self.updated_at.isoformat()
        my_dict['created_at'] =  self.created_at.isoformat()
        my_dict['__class__'] = self.__class__.__name__
        return my_dict

    def __str__(self):
        return "[BaseModel] ({}) {}".format(self.id, self.__dict__)
