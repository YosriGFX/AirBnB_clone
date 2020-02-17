#!/usr/bin/env python3
import uuid
from datetime import datetime
'''Base Model file'''


class BaseModel:
    '''BaseModel Class'''
    forme = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        '''__init___'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    self.__dict__[key] = datetime.strptime(
                                                            value,
                                                            BaseModel.forme
                                                        )
                else:
                    self.__dict__[key] = value

    def __str__(self):
        '''Return String'''
        return ("[{:s}] ({:s}) {}".format(
                                            self.__class__.__name__,
                                            self.id,
                                            self.__dict__
                                        ))

    def save(self):
        '''Save function'''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''To dictionary function'''
        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__['__class__'] = self.__class__.__name__
        return (self.__dict__)
