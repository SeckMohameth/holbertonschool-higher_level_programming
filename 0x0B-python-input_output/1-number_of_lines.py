#!/usr/bin/python3
def number_of_lines(filename=""):
    with open("my_file_0.txt", encoding="utf-8") as myFile:
        lines = 0
        for count in myFile:
            lines += 1
        return lines
