##
## EPITECH PROJECT, 2020
## 304
## File description:
## calc
##

import sys
import math
from dijkstra import dijkstra

### Engine ###
def algoEngine(map, wallChar, spaceChar):
    dijkstra(map)
    for line in map:
        for each in line:
            sys.stdout.write(each)
        print("")
