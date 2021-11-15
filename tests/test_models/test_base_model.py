#!/usr/bin/python3
"""Testing BaseModel"""

import unittest
from models.base_model import BaseModel
import pycodestyle


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

    def test_doc(self):
        """ Tests doc """
        self.assertIsNotNone(BaseModel.__doc__)

    def test_to_json(self):
        '''test to jason'''

    def test_kwarg(self):
        basemodel = BaseModel()
        self.assertEqual(type(basemodel).__name__, "BaseModel")
        self.assertTrue(hasattr(basemodel, "id"))
        self.assertTrue(hasattr(basemodel, "created_at"))
        self.assertTrue(hasattr(basemodel, "updated_at"))
        self.assertTrue(hasattr(basemodel, "__class__"))


if __name__ == '__main__':
    unittest.main()
