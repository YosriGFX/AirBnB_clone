#!/usr/bin/python3
from models.base_model import BaseModel

class user(BaseModel):
    """user class"""
    def __init__(self, email, password, first_name, last_name):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""
