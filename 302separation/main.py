##
## EPITECH PROJECT, 2020
## 302separation
## File description:
## main
##


import sys
from matrix import *
from degree import *

# ./302separation file [n | p1 p2]

def checkArguments():
    array = []

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Invalid number of args")
        exit(84)
    try:
        with open(sys.argv[1], "r") as file:
            array = file.readlines()
    except IOError:
        print("Invalid file")
        exit (84)
    if len(array) == 0:
        print("Empty file")
        exit (84)
    if len(array) >= 100:
        print("Too long file")
        exit (84)
    return array

### Get clean array of names ###
def getNames(array):
    names = []

    for connection in array:
        tmp = connection.rstrip()
        names += tmp.split(" is friends with ")
    names = list(dict.fromkeys(names))
    names = sorted(names)
    return(names)

def main():
    sys.setrecursionlimit(2000)
    array = checkArguments()
    names = getNames(array)

    if len(sys.argv) == 3:
        matrixEngine(array, names)
    else:
        degreeEngine(array, names, sys.argv[2], sys.argv[3])