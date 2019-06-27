#!/usr/bin/python3
class Base:
    "Class Base"
    __nb_objects = 0

    def __init__(self, id=None):
        "setting up init method"
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ saving csv"""
        pass

    @classmethod
    def load_from_file_csv(cls):
        """ csv file derserialze"""
        pass
