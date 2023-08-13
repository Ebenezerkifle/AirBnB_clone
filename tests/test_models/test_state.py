#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
import unittest
from models.base_model import BaseModel
from models.state import State
from models import storage
from datetime import datetime


class TestState_Intialization(unittest.TestCase):
    """Unittests for testing the intialization of State class"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.state = State()
        cls.state.name = "Abeni"

    def test_for_instantiation(self):
        """Tests instantiation of State class."""
        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(state), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(State, type(State()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(State(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(State().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(State().created_at))

    def test_has_attributes(self):
        self.assertTrue('id' in self.state.__dict__)
        self.assertTrue('created_at' in self.state.__dict__)
        self.assertTrue('updated_at' in self.state.__dict__)
        self.assertTrue('name' in self.state.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.state.name), str)

    def test_is_subclass(self):
        """Test that State is a subclass of BaseModel"""
        state = State()
        self.assertIsInstance(state, BaseModel)
        self.assertTrue(hasattr(state, "id"))
        self.assertTrue(hasattr(state, "created_at"))
        self.assertTrue(hasattr(state, "updated_at"))

    def test_name_attr(self):
        """Test that State has attr name, and it's an empty string"""
        state = State()
        self.assertTrue(hasattr(state, "name"))
        self.assertEqual(state.name, "")

    def test_str(self):
        """test that the str method has the correct output"""
        state = State()
        string = "[State] ({}) {}".format(state.id, state.__dict__)
        self.assertEqual(string, str(state))

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.state.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(State.__doc__)

    def test_save(self):
        self.state.save()
        self.assertNotEqual(self.state.created_at, self.state.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.state))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = State()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = State()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "State")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))


if __name__ == "__main__":
    unittest.main()
