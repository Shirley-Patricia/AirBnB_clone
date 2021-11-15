#!/usr/bin/python3
"""Testing FileStorage"""
import unittest
import models
from models.engine.file_storage import FileStorage
import pycodestyle


class TestFileStorage(unittest.TestCase):
    """Testing FileStorage class"""
    def test_instance(self):
        """testing if is an instance"""
        My_File = FileStorage()
        self.assertIsInstance(My_File, FileStorage)
