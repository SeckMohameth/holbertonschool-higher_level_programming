#!/usr/bin/python3
import sys
if __name__ == "__main__":
    mo = 0
    for x in sys.argv[1:]:
        mo += int(x)
    print(mo)
