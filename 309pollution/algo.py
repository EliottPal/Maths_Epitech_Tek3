##
## EPITECH PROJECT, 2021
## Maths
## File description:
## algo
##
import math
import sys

def getC(k, m):
    return math.factorial(m) / (math.factorial(k) * (math.factorial(m - k)))

def createHeatMap(n, fileArray):
    heatMap = list()

    for i in range(n):
        heatMap.append(list())
        for j in range(n):
            heatMap[i].append(0)
    for each in fileArray:
        y, x, value = int(each.split(';')[0]), int(each.split(';')[1]), int(each.split(';')[2])
        heatMap[y][x] = int(value)
    return heatMap

def makeCalc(n, heatMap, x, y):
    result = float(0)
    m1 = m2 = n - 1
    t1 = x  / m1
    t2 = y / m2

    for k1 in range(0, n):
        for k2 in range(0, n):
            tmp = getC(k1, m1) * getC(k2, m2) * (t1 ** k1 * ((1 - t1) ** (m1 - k1)))
            tmp *= (t2 ** k2 * ((1 - t2) ** (m2 - k2)))
            tmp *= heatMap[k1][k2]
            result += tmp
    return result

def engine(n, fileArray, x, y):
    heatMap = createHeatMap(n, fileArray)
    print("%.2f" % makeCalc(n, heatMap, x, y))
