#!/usr/bin/python3
"""Testing BaseModel"""

import unittest
import pycodestyle
import datetime
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """BaseModel Test"""

    def test_instance(self):
        """testing if is an instance"""
        basemodel = BaseModel()
        self.assertIsInstance(basemodel, BaseModel)

    def test_pycodestyle_BaseModel(self):
        """Testing for pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Check pycodestyle")

    def test_save_baseModel(self):
        """testing save method"""
        basemodel = BaseModel()
        basemodel.save()
        self.assertNotEqual(basemodel.created_at, basemodel.updated_at)
    
    def test_to_dict(self):
        """testing to_dict method"""
        basemodel = BaseModel()
        self.assertIs(type(basemodel.to_dict()), dict)
        self.assertIs(type(basemodel.updated_at), datetime.datetime)
        self.assertIs(type(basemodel.id), str)
        self.assertIs(type(basemodel.created_at), datetime.datetime)

    def test_doc(self):
        """Tests doc """
        self.assertIsNotNone(BaseModel.__doc__)
    
    def test_many_instances(self):
        """Testing attributes of instances"""
        basemodel1 = BaseModel()
        basemodel2 = BaseModel()
        self.assertNotEqual(basemodel1.id, basemodel2.id)
        self.assertNotEqual(basemodel1.created_at, basemodel2.created_at)

    def test_dictionary_attributes(self):
        basemodel = BaseModel()
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertTrue(hasattr(basemodel, "id"))
        self.assertTrue(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))


if __name__ == '__main__':
    unittest.main()
