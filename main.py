#!/usr/bin/python3
# base_model.py
from models import storage
from models.base_model import BaseModel
from models.user import User

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = User()
print(str(type(my_model)))
my_model.email = "ebenikifle"
my_model.password = '1238734'
my_model.save()
print(my_model)
