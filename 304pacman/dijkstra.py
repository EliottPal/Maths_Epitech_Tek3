##
## EPITECH PROJECT, 2020
## B-MAT-500-REN-5-1-304pacman-eliott.palueau
## File description:
## dijkstra
##
import sys
PACMAN = -4
GHOST = -3
WALL = -1
EMPTY = -2

def finder(array, find):
    x = 0
    y = 0

    for line in array:
        x = 0
        for sub in line:
            for charac in sub:
                if (charac == find):
                    return y, x
                x += 1
        y += 1

def printMap(array):
    for line in map:
        for each in line:
            print(each, '', '')
    print("")

def checker(array, passList, x, y, z):
    if y < 0 or x < 0:
        return False
    if y >= len(array) or x >= len(array[y]):
        return False
    if array[y][x] == PACMAN:
        return True
    if array[y][x] != EMPTY:
        return False
    array[y][x] = z + 1
    passList.append((x, y, z + 1))

def dijkstra(array):
    tmpGhost = finder(array, 'F')
    ghost = (tmpGhost[1], tmpGhost[0], 0)
    # print(ghost)
    pac = finder(array, 'P')
    prevNodes = list()
    prevNodes.append(ghost)
    finded = False
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = {'1': WALL, '0': EMPTY, 'F': GHOST, 'P': PACMAN}.get(array[i][j])

    while len(prevNodes) > 0:
        passList = list()
        for pac in prevNodes:
            if checker(array, passList, pac[0], pac[1] - 1, pac[2]) or checker(array, passList, pac[0] + 1, pac[1], pac[2]) or checker(array, passList, pac[0], pac[1] + 1, pac[2]) or checker(array, passList, pac[0] - 1, pac[1], pac[2]):
                finded = True
                break
        if finded == True:
            break
        prevNodes = passList
    # printMap(&array)
    for i in range(len(array)):
        for j in range(len(array[i])):
            array[i][j] = {WALL: sys.argv[2], EMPTY: sys.argv[3], GHOST: 'F', PACMAN: 'P'}.get(array[i][j], str(array[i][j] % 10))
