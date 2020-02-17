#!/usr/bin/env python3
from models.base_model import BaseModel
'''File Storage file'''

class FileStorage(BaseModel):
    '''FileStorage Class'''

    def __init__(self):
        '''__init__'''
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        '''return __objects'''
        return (self.__objects)

    def new(self, obj):
        '''new obj'''
        self.__objects = "%s" % (obj.__class__.__name__, obj.id)
