#!/usr/bin/python3
#__init__.py
"""Initialized the package"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
