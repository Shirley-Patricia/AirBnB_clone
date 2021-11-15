#!/usr/bin/python3
"""
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test class Review"""

    def setUp(self):
        """creating object"""
        self.My_review = Review()

    def test_type_amenity(self):
        """tests type class Review"""
        self.assertEqual(type(self.My_review), Review)

    def test_attr_basemod(self):
        """test attr inherites of BaseModel"""
        self.assertTrue(hasattr(self.My_review, "id"))
        self.assertTrue(hasattr(self.My_review, "created_at"))
        self.assertTrue(hasattr(self.My_review, "updated_at"))
        self.assertTrue(hasattr(self.My_review, "__class__"))

    def test_attr_class(self):
        """test attr of class"""
        self.assertTrue(hasattr(self.My_review, "place_id"))
        self.assertEqual(type(self.My_review.place_id), str)
        self.assertTrue(hasattr(self.My_review, "user_id"))
        self.assertEqual(type(self.My_review.user_id), str)
        self.assertTrue(hasattr(self.My_review, "text"))
        self.assertEqual(type(self.My_review.text), str)


if __name__ == '__main__':
    unittest.main()
