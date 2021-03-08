##
## EPITECH PROJECT, 2020
## B-MAT-500-REN-5-1-306radiator-eliott.palueau
## File description:
## main
##

import sys
from algo import *

# USAGE
# 	./306radiator n ir jr [i j]
# DESCRIPTION
# 	n           size of the room
# 	(ir, jr)    coordinates of the radiator
# 	(i, j)      coordinates of a point in the room

# A check
# Chauffage colonne 0 ou N-1
# Chauffage derniere ligne

### Error management ###
def checkArguments():

    if len(sys.argv) != 6 and len(sys.argv) != 4:
        print("Invalid number of args")
        exit(84)
    for arg in range(1, len(sys.argv)):
        try:
            if not int(sys.argv[arg]):
                pass
        except:
            print("Invalid argument, number excepted")
            exit(84)
    if not int(sys.argv[1]) >= 3:
        print("Invalid room size")
        exit(84)
    if not 1 <= int(sys.argv[2]) or not int(sys.argv[3]) <= (int(sys.argv[1]) - 2):
        print("Invalid radiator coordinates")
        exit(84)
    if int(sys.argv[2]) == 0 or int(sys.argv[2]) == (int(sys.argv[1]) - 1):
        print("Invalid radiator coordinates")
        exit(84)
    if len(sys.argv) == 6:
       if not 1 <= int(sys.argv[4]) or not int(sys.argv[5]) <= (int(sys.argv[1]) - 2):
           print("Invalid point coordinates")
           exit(84)

def main():
    checkArguments()

    n = int(sys.argv[1])
    ir = int(sys.argv[2])
    jr = int(sys.argv[3])

    X = findXMatrix(n, ir, jr, (len(sys.argv) == 4))

    if len(sys.argv) == 6:
        i = int(sys.argv[4])
        j = int(sys.argv[5])
        temperatureAtIJ(X, n, i, j)


