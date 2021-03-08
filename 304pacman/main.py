##
## EPITECH PROJECT, 2020
## 304
## File description:
## main
##

import sys
from calc import *


# USAGE
#	./304pacman file c1 c2
# DESCRIPTION
# 	file    file describing the board, using the following characters:
# 		'0' for an empty square
# 		'1' for a wall
# 		'F' for the ghost's position
# 		'P' for Pacman's position.
# 	c1      character to display for a wall
# 	c2      character to display for an empty space.


### Error management ###
def checkArguments():
    array = []

    if len(sys.argv) != 4:
        print("Invalid number of args")
        exit(84)
    if len(sys.argv[2]) > 1 or len(sys.argv[3]) > 1:
        print("Invalid arguments (only one character si needed)")
        exit(84)
    try:
        with open(sys.argv[1], "r") as file:
            i = 0
            for line in file:
                for each in line.rsplit():
                    array.append(list())
                    for charac in each:
                        array[i].append(charac)
                i += 1
    except IOError:
        print("Invalid file")
        exit (84)
    if len(array) == 0:
        print("Empty File")
        exit(84)
    return array

### Check if map is valid ###
def checkMap(map):
    checkPacman = False
    checkGhost = False

    for i in map:
        for j in i:
            for c in j:
                if c != '0' and c != '1' and c != 'P' and c != 'F':
                    print("Invalid map (invalid character found)")
                    exit(84)
                if c == 'P' and checkPacman == True:
                    exit(84)
                if c == 'F' and checkGhost == True:
                    exit(84)
                if c == 'P':
                    checkPacman = True
                if c == 'F':
                    checkGhost = True

    if checkPacman == False or checkGhost == False:
        print("Invalid map (missing pacman/ghost)")
        exit(84)
    length = len(map[0])
    for line in map:
        if len(line) != length:
            sys.stderr.write("Length problem")
            exit(84)

def main():
    array = checkArguments()
    checkMap(array)
    algoEngine(array, sys.argv[2], sys.argv[3])

