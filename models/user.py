#!/usr/bin/python3
# user.py
"""The representation of a user class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents the User Class which is a subclass of BaseModel class"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
