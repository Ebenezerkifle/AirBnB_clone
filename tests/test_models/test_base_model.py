#!/usr/bin/python3
"""Defines unittests for models/base_model.py.
Unittest classes:
    TestBaseModel_instantiation
    TestBase_Instance_Print
    TestBaseModel_save
    TestBase_from_json_string
    TestBaseModel_to_dict
"""
import datetime
import unittest

from models.base_model import BaseModel
from models import storage


class TestBaseModel_Instantiation(unittest.TestCase):
    """Unittests for testing instantiation of the BaseModel class."""

    # tests if the instance has an attribute called id
    def test_ContainsId(self):
        """Test If the id attribute exists"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, 'id'))

    # tests if the id is string.
    def test_IdType(self):
        """Test Id type"""
        b1 = BaseModel()
        self.assertEqual(type(b1.id), str)

    # test case for checking if the instance of a class has type of BaseModel class
    def test_Instance(self):
        """Test Instance"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
        self.assertEqual(
            str(type(b1), "<class 'models.base_model.BaseModel'>"))
        self.assertEqual(issubclass(type(b1), BaseModel))

    # test case to check if the two instances have the same id
    def test_CompareTwoInstancesId(self):
        """Test the the difference of id's of two instances of BaseModel class"""
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)

    # test case to check the validity of uuid
    def test_uuid(self):
        """Test that id is a valid uuid"""
        b1 = BaseModel()
        b2 = BaseModel()
        for inst in [b1, b2]:
            uuid = inst.id
            with self.subTest(uuid=uuid):
                self.assertIs(type(uuid), str)
                self.assertRegex(uuid,
                                 '^[0-9a-f]{8}-[0-9a-f]{4}'
                                 '-[0-9a-f]{4}-[0-9a-f]{4}'
                                 '-[0-9a-f]{12}$')
        self.assertNotEqual(b1.id, b2.id)

    # test case to check if the id is unique.
    def test_uniq_id(self):
        """Tests for unique user ids."""
        u = [BaseModel().id for i in range(1000)]
        self.assertEqual(len(set(u)), len(u))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(BaseModel(), storage.all().values())

    # test case to check if the attribute created_at exists
    def test_Contains_created_at(self):
        """Test if the attribute created_at exists"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, 'created_at'))

    # test case to check the type of created_at
    def test_Type_of_created_at(self):
        """Test for the data type of created_at"""
        b1 = BaseModel()
        self.assertIsInstance(b1.created_at, datetime)

    # test case to check if the attribute updated_at exists
    def test_Contains_updated_at(self):
        """Test if the attribute updated_at exists"""
        b1 = BaseModel()
        self.assertTrue(hasattr(b1, 'updated_at'))

    # test case to check the type of updated_at
    def test_Type_of_updated_at(self):
        """Test for the data type of updated_at"""
        b1 = BaseModel()
        self.assertIsInstance(b1.updated_at, datetime)


# The entry point.
if __name__ == '__main__':
    unittest.main()
