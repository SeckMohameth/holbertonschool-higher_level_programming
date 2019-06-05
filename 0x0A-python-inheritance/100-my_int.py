#!/usr/bin/python3
class MyInt(int):
    def __eq__(self, other):
        return int(self) is not other

    def __ne__(self, other):
        return int(self) is other
