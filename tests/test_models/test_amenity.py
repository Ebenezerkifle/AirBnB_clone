#!/usr/bin/python3
"""Defines unittests for models/state.py.
"""
import unittest
from models.base_model import BaseModel
from models.amenity import Amenity
from models import storage
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Unittests for testing the intialization of State class"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.amen = Amenity()
        cls.amen.name = "Aymane"

    def test_for_instantiation(self):
        """Tests instantiation of Amenity class."""
        am = Amenity()
        self.assertEqual(str(type(am)),
                         "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(am, Amenity)
        self.assertTrue(issubclass(type(am), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_has_attributes(self):
        self.assertTrue('id' in self.amen.__dict__)
        self.assertTrue('created_at' in self.amen.__dict__)
        self.assertTrue('updated_at' in self.amen.__dict__)
        self.assertTrue('name' in self.amen.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.amen.name), str)

    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        am = Amenity()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attr name, and it's an empty string"""
        am = Amenity()
        self.assertTrue(hasattr(am, "name"))
        self.assertEqual(am.name, "")

    def test_str(self):
        """test that the str method has the correct output"""
        am = Amenity()
        string = "[Amenity] ({}) {}".format(am.id, am.__dict__)
        self.assertEqual(string, str(am))

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amen.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Amenity.__doc__)

    def test_save(self):
        self.amen.save()
        self.assertNotEqual(self.amen.created_at, self.amen.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.amen))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Amenity()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = Amenity()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Amenity")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))


if __name__ == "__main__":
    unittest.main()
