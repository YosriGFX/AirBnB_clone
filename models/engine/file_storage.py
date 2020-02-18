#!/usr/bin/env python3
from models.base_model import BaseModel
import json
'''File Storage file'''


class FileStorage():
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
        self.__objects[
            "{}.{}".format(obj.__class__.__name__, obj.id)
            ] = obj

    def save(self):
        '''save json'''
        dict_exp = {
                        obj: self.__objects[obj].to_dict()
                        for obj in self.__objects.keys()
        }
        json_exp = open(self.__file_path, "w")
        json_exp.write(json.dumps(dict_exp))
        json_exp.close()
