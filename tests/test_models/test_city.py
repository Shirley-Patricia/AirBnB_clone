#!/usr/bin/python3
"""
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class Testcity(unittest.TestCase):
    """
    """
def setUp(self):
        """creating object"""
        self.My_city = City()

        def test_type_city(self):
            """tests type class city"""
            self.assertEqual(type(self.My_city), City)

        def test_attr_basemod(self):
            """test attr inherites of BaseModel"""
            self.assertTrue(hasattr(self.My_city, "id"))
            self.assertTrue(hasattr(self.My_city, "created_at"))
            self.assertTrue(hasattr(self.My_city, "updated_at"))
            self.assertTrue(hasattr(self.My_city, "__class__"))

        def test_attr_class(self):
            """test attr of class"""
            self.assertTrue(hasattr(self.My_city, "name"))
            self.assertEqual(type(self.My_city.name), str)


if __name__ == '__main__':
    unittest.main()