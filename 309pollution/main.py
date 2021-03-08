##
## EPITECH PROJECT, 2021
## Maths
## File description:
## main
##

import sys
from algo import *

# USAGE
#   ./309pollution n file x y
# DESCRIPTION
#   n       number of points on the grid axis
#   file    csv file containing the data points x;y;p
#   x       abscissa of the point whose pollution level we want to know
#   y       ordinate of the point whose pollution level we want to know

### Error management ###
def checkArguments():
    array = []
    ## Check arguments
    if len(sys.argv) != 5:
        print("Invalid number of args")
        exit(84)
    try:
        if not float(sys.argv[4]) or not float(sys.argv[3]) or not int(sys.argv[1]):
            pass
    except:
        print("Invalid argument, number excepted")
        exit(84)
    # Check number of points
    try:
        if int(sys.argv[1]) <= 0:
            pass
    except:
        print("Invalid argument, number of points must be positive")
        exit(84)
    # Check abscissa
    if not float(sys.argv[3]) >= 0 or not float(sys.argv[3]) <= (int(sys.argv[1]) - 1):
        print("Invalid abscissa, coordinates must be between 0 and n-1")
        exit(84)
    # Check ordinate
    if not float(sys.argv[4]) >= 0 or not float(sys.argv[4]) <= (int(sys.argv[1]) - 1):
        print("Invalid ordinate, coordinates must be between 0 and n-1")
        exit(84)
    ## Check file
    try:
        with open(sys.argv[2], "r") as file:
            for line in file:
                array += line.split('\n')
    except IOError:
        print("Invalid file")
        exit (84)
    if len(array) == 0:
        print("Empty File")
        exit(84)
    array = filter(None, array)
    tmp = list()
    for each in array:
        tmp.append(each)
    return tmp

def checkFile(array):
    tmp = ""
    for line in array:
        if line[-1] == ';':
            print("Invalid line: line ending by \";\"")
            exit(84)
        tmp = line.split(';')
        if len(tmp) < 3:
            print("Invalid line: not enough information")
            exit(84)
        for value in tmp:
            try:
                if not int(value):
                    pass
            except:
                print("Invalid value, number excepted")
                exit(84)

def main():
    array = checkArguments()
    checkFile(array)

    n = int(sys.argv[1])
    x = float(sys.argv[3])
    y = float(sys.argv[4])

    engine(n, array, x, y)