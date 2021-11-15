#!/usr/bin/python3
"""Testing Place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test class Place"""

    def setUp(self):
        """creating object"""
        self.My_place = Place()

    def test_type_amenity(self):
        """tests type class Place"""
        self.assertEqual(type(self.My_place), Place)

    def test_attr_basemod(self):
        """test attr inherites of BaseModel"""
        self.assertTrue(hasattr(self.My_place, "id"))
        self.assertTrue(hasattr(self.My_place, "created_at"))
        self.assertTrue(hasattr(self.My_place, "updated_at"))
        self.assertTrue(hasattr(self.My_place, "__class__"))

    def test_attr_class(self):
        """test attr of class type str"""
        self.assertTrue(hasattr(self.My_place, "city_id"))
        self.assertEqual(type(self.My_place.city_id), str)
        self.assertTrue(hasattr(self.My_place, "user_id"))
        self.assertEqual(type(self.My_place.user_id), str)
        self.assertTrue(hasattr(self.My_place, "name"))
        self.assertEqual(type(self.My_place.name), str)
        self.assertTrue(hasattr(self.My_place, "description"))
        self.assertEqual(type(self.My_place.description), str)

    def test_attr_class(self):
        """test attr of class type int"""
        self.assertTrue(hasattr(self.My_place, "number_rooms"))
        self.assertEqual(type(self.My_place.number_rooms), int)
        self.assertTrue(hasattr(self.My_place, "number_bathrooms"))
        self.assertEqual(type(self.My_place.number_bathrooms), int)
        self.assertTrue(hasattr(self.My_place, "max_guest"))
        self.assertEqual(type(self.My_place.max_guest), int)
        self.assertTrue(hasattr(self.My_place, "price_by_night"))
        self.assertEqual(type(self.My_place.price_by_night), int)

    def test_attr_class(self):
        """test attr of class type float"""
        self.assertTrue(hasattr(self.My_place, "latitude"))
        self.assertEqual(type(self.My_place.latitude), float)
        self.assertTrue(hasattr(self.My_place, "longitude"))
        self.assertEqual(type(self.My_place.longitude), float)

    def test_attr_class(self):
        """test attr of class type list"""
        self.assertTrue(hasattr(self.My_place, "amenity_ids"))
        self.assertEqual(type(self.My_place.amenity_ids), list)


if __name__ == '__main__':
    unittest.main()
