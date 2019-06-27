#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return(self.__dict__)

        mylist = {}
        for key, val, in self.__dict__.items():
            if key in attrs:
                mylist[key] = val
        return(mylist)

    def reload_from_json(self, json):
        for key, val in json.items():
            setattr(self, key, val)
