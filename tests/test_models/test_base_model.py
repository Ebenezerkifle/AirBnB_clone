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
import json
import re
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

    def test_datetime_created(self):
        """Tests if updated_at & created_at are current at creation."""
        date_now = datetime.now()
        b1 = BaseModel()
        diff = b1.updated_at - b1.created_at
        self.assertTrue(abs(diff.total_seconds()) < 0.01)
        diff = b1.created_at - date_now
        self.assertTrue(abs(diff.total_seconds()) < 0.1)

    def test_id_is_public_str(self):
        """Test if the attribute id is public and string"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at_is_public(self):
        """Test if the attribute created_at is public and datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at_is_public(self):
        """Test if the attribute updated_at is public and datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_str_representation(self):
        dt = datetime.today()
        dt_repr = repr(dt)
        b1 = BaseModel()
        b1.id = "123456"
        b1.created_at = b1.updated_at = dt
        b1str = b1.__str__()
        self.assertIn("[BaseModel] (123456)", b1str)
        self.assertIn("'id': '123456'", b1str)
        self.assertIn("'created_at': " + dt_repr, b1str)
        self.assertIn("'updated_at': " + dt_repr, b1str)

    def test_args_unused(self):
        b1 = BaseModel(None)
        self.assertNotIn(None, b1.__dict__.values())

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            BaseModel(id=None, created_at=None, updated_at=None)

    def test_instantiation_with_args_and_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        b1 = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(b1.id, "345")
        self.assertEqual(b1.created_at, dt)
        self.assertEqual(b1.updated_at, dt)


class TestBaseModel_Instance_Print(unittest.TestCase):
    """Unittest for testing the __str__method."""

    # test for the validity of return value
    def test_str_return(self):
        """Test for the return value of __str__ method."""
        b = BaseModel()
        abeni = "[{}] ({}) {}".format("BaseModel", b.id, str(b.__dict__))
        self.assertEqual(abeni, str(b))

    # test if the method has the correct output
    def test_str(self):
        """Test if the method has the correct output"""
        b = BaseModel()
        string = "[BaseModel] ({}) {}".format(b.id, b.__dict__)
        self.assertEqual(string, str(b))

    def test_of_str(self):
        """Test for __str__ method"""
        b1 = BaseModel()
        rex = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        res = rex.match(str(b1))
        self.assertIsNotNone(res)
        self.assertEqual(res.group(1), "BaseModel")
        self.assertEqual(res.group(2), b1.id)
        s = res.group(3)
        s = re.sub(r"(datetime\.datetime\([^)]*\))", "'\\1'", s)
        d = json.loads(s.replace("'", '"'))
        d2 = b1.__dict__.copy()
        d2["created_at"] = repr(d2["created_at"])
        d2["updated_at"] = repr(d2["updated_at"])
        self.assertEqual(d, d2)


class TestBaseModel_Save_Method(unittest.TestCase):
    """Unittest for testing the savae method."""


# The entry point.
if __name__ == '__main__':
    unittest.main()
