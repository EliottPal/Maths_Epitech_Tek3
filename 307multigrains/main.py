##
## EPITECH PROJECT, 2020
## Maths
## File description:
## main
##

import sys
from new import *

# USAGE
#   ./307multigrains n1 n2 n3 n4 po pw pc pb ps
# DESCRIPTION
#   n1      number of tons of fertilizer F1
#   n2      number of tons of fertilizer F2
#   n3      number of tons of fertilizer F3
#   n4      number of tons of fertilizer F4
#   po      price of one unit of oat
#   pw      price of one unit of wheat
#   pc      price of one unit of corn
#   pb      price of one unit of barley
#   ps      price of one unit of soy


### Error management ###
def checkArguments():

    if len(sys.argv) != 10:
        print("Invalid number of args")
        exit(84)
    for arg in range(1, len(sys.argv)):
        try:
            if not int(sys.argv[arg]):
                pass
        except:
            print("Invalid argument, number excepted")
            exit(84)
        if int(sys.argv[arg]) < 0:
            print("Invalid value, positive value expected")
            exit(84)

def main():
    checkArguments()

    n1 = int(sys.argv[1])
    n2 = int(sys.argv[2])
    n3 = int(sys.argv[3])
    n4 = int(sys.argv[4])
    po = int(sys.argv[5])
    pw = int(sys.argv[6])
    pc = int(sys.argv[7])
    pb = int(sys.argv[8])
    ps = int(sys.argv[9])

    algo(n1, n2, n3, n4, po, pw, pc, pb, ps)