#!/usr/bin/python3
"""Testing Amenity class"""
import os
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Tests class Amenity"""

    def setUp(self):
        """creating object"""
        self.My_amenity = Amenity()

    def test_type_amenity(self):
        """tests type class Amenity"""
        self.assertEqual(type(self.My_amenity), Amenity)

    def test_attr_basemod(self):
        """test attr inherites of BaseModel"""
        self.assertTrue(hasattr(self.My_amenity, "id"))
        self.assertTrue(hasattr(self.My_amenity, "created_at"))
        self.assertTrue(hasattr(self.My_amenity, "updated_at"))
        self.assertTrue(hasattr(self.My_amenity, "__class__"))

    def test_attr_class(self):
        """test attr of class"""
        self.assertTrue(hasattr(self.My_amenity, "name"))
        self.assertEqual(type(self.My_amenity.name), str)


if __name__ == '__main__':
    unittest.main()
