import sys

def warning(string):
    print(" :: warning:", string)

def error(string):
    print(" :: error:  ", string)
    sys.exit(0)
