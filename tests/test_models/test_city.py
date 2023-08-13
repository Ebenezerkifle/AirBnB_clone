#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models import storage
from datetime import datetime


class TestCity(unittest.TestCase):
    """Unittests for testing the intialization of State class"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.city = City()
        cls.city.name = "Aymane"
        cls.city.state_id = ""

    def test_for_instantiation(self):
        """Tests instantiation of City class."""
        am = City()
        self.assertEqual(str(type(am)),
                         "<class 'models.city.City'>")
        self.assertIsInstance(am, City)
        self.assertTrue(issubclass(type(am), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(City, type(City()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(City(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(City().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(City().created_at))

    def test_has_attributes(self):
        self.assertTrue('id' in self.city.__dict__)
        self.assertTrue('created_at' in self.city.__dict__)
        self.assertTrue('updated_at' in self.city.__dict__)
        self.assertTrue('name' in self.city.__dict__)
        self.assertTrue('state_id' in self.city.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.city.name), str)
        self.assertIs(type(self.city.state_id), str)

    def test_is_subclass(self):
        """Test that City is a subclass of BaseModel"""
        am = City()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))

    def test_name_attr(self):
        """Test that City has attr name, and it's an empty string"""
        am = City()
        self.assertTrue(hasattr(am, "name"))
        self.assertEqual(am.name, "")

    def test_state_id_attr(self):
        """Test that City has attr state_id, and it's an empty string"""
        am = City()
        self.assertTrue(hasattr(am, "state_id"))
        self.assertEqual(am.state_id, "")

    def test_str(self):
        """test that the str method has the correct output"""
        am = City()
        string = "[City] ({}) {}".format(am.id, am.__dict__)
        self.assertEqual(string, str(am))

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.city.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(City.__doc__)

    def test_save(self):
        self.city.save()
        self.assertNotEqual(self.city.created_at, self.city.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.city))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = City()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = City()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "City")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))


if __name__ == "__main__":
    unittest.main()
