#!/usr/bin/python3
"""
Creating of class Review that inherit from BaseModel
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class Review with the following public class attributes"""

    place_id = ""
    user_id = ""
    text = ""
