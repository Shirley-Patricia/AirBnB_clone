#!/usr/bin/python3
"""Testing BaseModel"""

import unittest
import pycodestyle
import datetime
from models.base_model import BaseModel



class TestBaseModel(unittest.TestCase):
    """BaseModel Test"""

    def test_pycodestyle_BaseModel(self):
        """Testing for pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=True)
        p = style.check_files(['models/base_model.py'])
        self.assertEqual(p.total_errors, 0, "Check pycodestyle")

    def test_save_baseModel(self):
        basemodel = BaseModel()
        basemodel.save()
        self.assertNotEqual(basemodel.created_at, basemodel.updated_at)
    
    def test_to_dict(self):
        basemodel = BaseModel()
        self.assertIs(type(basemodel.to_dict()), dict)
        self.assertIs(type(basemodel.updated_at), datetime.datetime)
        self.assertIs(type(basemodel.id), str)
        self.assertIs(type(basemodel.created_at), datetime.datetime)

    def test_doc(self):
        """ Tests doc """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_dictionary(self):
        basemodel = BaseModel()
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertTrue(hasattr(basemodel, "id"))
        self.assertTrue(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))


if __name__ == '__main__':
    unittest.main()
