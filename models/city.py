#!/usr/bin/python3
"""
Creating of class City that inherit from BaseModel
"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class City with the following public class attributes"""

    state_id = ""
    name = ""
