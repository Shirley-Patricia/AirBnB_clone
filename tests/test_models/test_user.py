#!/usr/bin/python3
"""Testing User"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test class User"""

    def setUp(self):
        """creating object"""
        self.My_user = User()

    def test_type_amenity(self):
        """tests type class User"""
        self.assertEqual(type(self.My_user), User)

    def test_attr_basemod(self):
        """test attr inherites of BaseModel"""
        self.assertTrue(hasattr(self.My_user, "id"))
        self.assertTrue(hasattr(self.My_user, "created_at"))
        self.assertTrue(hasattr(self.My_user, "updated_at"))
        self.assertTrue(hasattr(self.My_user, "__class__"))

    def test_attr_class(self):
        """test attr of class"""
        self.assertTrue(hasattr(self.My_user, "email"))
        self.assertEqual(type(self.My_user.email), str)
        self.assertTrue(hasattr(self.My_user, "password"))
        self.assertEqual(type(self.My_user.password), str)
        self.assertTrue(hasattr(self.My_user, "first_name"))
        self.assertEqual(type(self.My_user.first_name), str)
        self.assertTrue(hasattr(self.My_user, "last_name"))
        self.assertEqual(type(self.My_user.last_name), str)


if __name__ == '__main__':
    unittest.main()
