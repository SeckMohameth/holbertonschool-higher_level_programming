#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    if nb_lines <= 0 or nb_lines >= len(filename):
        with open(filename, encoding="utf-8") as myFile:
            print(myFile.read(), end="")
    count = 0
    with open(filename, encoding="utf-8") as myFile:
        for lines in filename:
            while count < nb_lines:
                print(myFile.readline(), end="")
                count += 1
