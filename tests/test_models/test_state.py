#!/usr/bin/python3
"""
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    """
    def setUp(self):
        """creating object"""
        self.My_state = State()

        def test_type_state(self):
            """tests type class state"""
            self.assertEqual(type(self.My_state), State)

        def test_attr_basemod(self):
            """test attr inherites of BaseModel"""
            self.assertTrue(hasattr(self.My_state, "id"))
            self.assertTrue(hasattr(self.My_state, "created_at"))
            self.assertTrue(hasattr(self.My_state, "updated_at"))
            self.assertTrue(hasattr(self.My_state, "__class__"))

        def test_attr_class(self):
            """test attr of class"""
            self.assertTrue(hasattr(self.My_state, "name"))
            self.assertEqual(type(self.My_state.name), str)


if __name__ == '__main__':
    unittest.main()
