#!/usr/bin/env python3
import uuid
from datetime import datetime
'''Base model file'''


class BaseModel:
    '''BaseModel Class'''

    def __init__(self):
        '''__init___'''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

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
