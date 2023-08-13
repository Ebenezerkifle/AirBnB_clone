#!/usr/bin/python3
"""Defines unittests for models/place.py.
"""
import unittest
from models.base_model import BaseModel
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Unittests for testing the intialization of State class"""

    @classmethod
    def setUpClass(cls):
        """Setup the unittest"""
        cls.amen = Place()
        cls.amen.city_id = "0938475"
        cls.amen.user_id = "asl;dkfja"
        cls.amen.name = "Aymane"
        cls.amen.description = "some description here..."
        cls.amen.number_rooms = 10
        cls.amen.number_bathrooms = 5
        cls.amen.max_guest = 400
        cls.amen.price_by_night = 100
        cls.amen.latitude = 42.134
        cls.amen.longitude = 42.134
        cls.amen.amenity_ids = []

    def test_for_instantiation(self):
        """Tests instantiation of Place class."""
        am = Place()
        self.assertEqual(str(type(am)),
                         "<class 'models.place.Place'>")
        self.assertIsInstance(am, Place)
        self.assertTrue(issubclass(type(am), BaseModel))

    def test_no_args_instantiates(self):
        self.assertEqual(Place, type(Place()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Place(), storage.all().values())

    def test_id_is_public_str(self):
        self.assertEqual(str, type(Place().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Place().created_at))

    def test_has_attributes(self):
        self.assertTrue('id' in self.amen.__dict__)
        self.assertTrue('created_at' in self.amen.__dict__)
        self.assertTrue('updated_at' in self.amen.__dict__)
        self.assertTrue('name' in self.amen.__dict__)
        self.assertTrue('city_id' in self.amen.__dict__)
        self.assertTrue('user_id' in self.amen.__dict__)
        self.assertTrue('description' in self.amen.__dict__)
        self.assertTrue('number_rooms' in self.amen.__dict__)
        self.assertTrue('number_bathrooms' in self.amen.__dict__)
        self.assertTrue('max_guest' in self.amen.__dict__)
        self.assertTrue('price_by_night' in self.amen.__dict__)
        self.assertTrue('latitude' in self.amen.__dict__)
        self.assertTrue('longitude' in self.amen.__dict__)
        self.assertTrue('amenity_ids' in self.amen.__dict__)

    def test_attributes_are_string(self):
        self.assertIs(type(self.amen.name), str)
        self.assertIs(type(self.amen.city_id), str)
        self.assertIs(type(self.amen.user_id), str)
        self.assertIs(type(self.amen.description), str)

    def test_attributes_are_int(self):
        self.assertIs(type(self.amen.number_bathrooms), int)
        self.assertIs(type(self.amen.number_rooms), int)
        self.assertIs(type(self.amen.max_guest), int)
        self.assertIs(type(self.amen.price_by_night), int)

    def test_attributes_are_float(self):
        self.assertIs(type(self.amen.latitude), float)
        self.assertIs(type(self.amen.longitude), float)
        self.assertIs(type(self.amen.amenity_ids), list)

    def test_is_subclass(self):
        """Test that Place is a subclass of BaseModel"""
        am = Place()
        self.assertIsInstance(am, BaseModel)
        self.assertTrue(hasattr(am, "id"))
        self.assertTrue(hasattr(am, "created_at"))
        self.assertTrue(hasattr(am, "updated_at"))

    def test_amenity_ids_attr(self):
        """Test that Place has attr amenity_ids, and it's an empty list"""
        am = Place()
        self.assertTrue(hasattr(am, "amenity_ids"))
        self.assertEqual(am.amenity_ids, [])

    def test_latlong_attr(self):
        """Test that Place has attr latitude, and it's a float with default value 0.0"""
        am = Place()
        self.assertTrue(hasattr(am, "latitude"))
        self.assertEqual(am.latitude, 0.0)
        self.assertTrue(hasattr(am, "longitude"))
        self.assertEqual(am.longitude, 0.0)

    def test_name_attr(self):
        """Test that Place has attr name, and it's an empty string"""
        am = Place()
        self.assertTrue(hasattr(am, "name"))
        self.assertEqual(am.name, "")

    def test_city_id_attr(self):
        """Test that Place has attr city_id, and it's an empty string"""
        am = Place()
        self.assertTrue(hasattr(am, "city_id"))
        self.assertEqual(am.city_id, "")

    def test_user_id_attr(self):
        """Test that Place has attr user_id, and it's an empty string"""
        am = Place()
        self.assertTrue(hasattr(am, "user_id"))
        self.assertEqual(am.user_id, "")

    def test_description_attr(self):
        """Test that Place has attr description, and it's an empty string"""
        am = Place()
        self.assertTrue(hasattr(am, "description"))
        self.assertEqual(am.description, "")

    def test_number_bathrooms_attr(self):
        """Test that Place has attr number_bathrooms, and it's an integer with value 0"""
        am = Place()
        self.assertTrue(hasattr(am, "number_bathrooms"))
        self.assertEqual(am.number_bathrooms, 0)

    def test_number_rooms_attr(self):
        """Test that Place has attr number_rooms, and it's an integer with value 0"""
        am = Place()
        self.assertTrue(hasattr(am, "number_rooms"))
        self.assertEqual(am.number_rooms, 0)

    def test_max_guest_attr(self):
        """Test that Place has attr max_guest, and it's an integer with value 0"""
        am = Place()
        self.assertTrue(hasattr(am, "max_guest"))
        self.assertEqual(am.max_guest, 0)

    def test_price_by_night_attr(self):
        """Test that Place has attr price_by_night, and it's an integer with value 0"""
        am = Place()
        self.assertTrue(hasattr(am, "price_by_night"))
        self.assertEqual(am.price_by_night, 0)

    def test_str(self):
        """test that the str method has the correct output"""
        am = Place()
        string = "[Place] ({}) {}".format(am.id, am.__dict__)
        self.assertEqual(string, str(am))

    def test_is_subclass(self):
        self.assertTrue(issubclass(self.amen.__class__, BaseModel))

    def checking_for_doc(self):
        self.assertIsNotNone(Place.__doc__)

    def test_save(self):
        self.amen.save()
        self.assertNotEqual(self.amen.created_at, self.amen.updated_at)

    def test_to_dict(self):
        self.assertTrue('to_dict' in dir(self.amen))

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attrs"""
        u = Place()
        new_d = u.to_dict()
        self.assertEqual(type(new_d), dict)
        for attr in u.__dict__:
            self.assertTrue(attr in new_d)
            self.assertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        u = Place()
        new_d = u.to_dict()
        self.assertEqual(new_d["__class__"], "Place")
        self.assertEqual(type(new_d["created_at"]), str)
        self.assertEqual(type(new_d["updated_at"]), str)
        self.assertEqual(new_d["created_at"], u.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], u.updated_at.strftime(t_format))


if __name__ == "__main__":
    unittest.main()
