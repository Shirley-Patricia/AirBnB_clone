#!/usr/bin/python3
"""
Creating of class User that records information about user and
inherits of Basemodel
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class User with the following public class attribute"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
