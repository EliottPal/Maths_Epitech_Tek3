##
## EPITECH PROJECT, 2021
## B-MAT-500-REN-5-1-308reedpipes-eliott.palueau
## File description:
## main
##

import sys
from algo import *

# USAGE
#   ./308reedpipes r0 r5 r10 r15 r20 n
# DESCRIPTION
#   r0      radius (in cm) of pipe at the 0cm abscissa
#   r5      radius (in cm) of pipe at the 5cm abscissa
#   r10     radius (in cm) of pipe at the 10cm abscissa
#   r15     radius (in cm) of pipe at the 15cm abscissa
#   r20     radius (in cm) of pipe at the 20cm abscissa
#   n       number of points needed to display the radius

### Error management ###
def checkArguments():

    if len(sys.argv) != 7:
        print("Invalid number of args")
        exit(84)
    for arg in range(1, len(sys.argv)):
        try:
            if not float(sys.argv[arg]):
                pass
        except:
            print("Invalid argument, number excepted")
            exit(84)
        if float(sys.argv[arg]) <= 0:
            print("Invalid value")
            exit(84)

def main():
    checkArguments()

    r0 = float(sys.argv[1])
    r5 = float(sys.argv[2])
    r10 = float(sys.argv[3])
    r15 = float(sys.argv[4])
    r20 = float(sys.argv[5])
    n = int(sys.argv[6])

    algo(r0, r5, r10, r15, r20, n)