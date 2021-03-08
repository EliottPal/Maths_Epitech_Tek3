##
## EPITECH PROJECT, 2021
## 307multigrains
## File description:
## new
##

def tabCerealsNeeds():
    cereals = list()

    cereals.append([1, 1, 2, 0])
    cereals.append([0, 2, 1, 0])
    cereals.append([1, 0, 0, 3])
    cereals.append([0, 1, 1, 1])
    cereals.append([2, 0, 0, 2])
    return cereals

def creatingMatrix(nList, pList):
    cereals = tabCerealsNeeds()
    matrix = [list()] * 5

    matrix[0] = [cereals[0][0], cereals[1][0], cereals[2][0], cereals[3][0], cereals[4][0], 1, 0, 0, 0, nList[0]]
    matrix[1] = [cereals[0][1], cereals[1][1], cereals[2][1], cereals[3][1], cereals[4][1], 0, 1, 0, 0, nList[1]]
    matrix[2] = [cereals[0][2], cereals[1][2], cereals[2][2], cereals[3][2], cereals[4][2], 0, 0, 1, 0, nList[2]]
    matrix[3] = [cereals[0][3], cereals[1][3], cereals[2][3], cereals[3][3], cereals[4][3], 0, 0, 0, 1, nList[3]]
    matrix[4] = [-pList[0], -pList[1], -pList[2], -pList[3], -pList[4], 0, 0, 0, 0, 0]
    return matrix

def findPivot(matrix):
    if (len(matrix) <= 0 or len(matrix[0]) <= 5):
        return (-1, -1)
    valY, valX = len(matrix), len(matrix[0])
    line = matrix[valY - 1]
    copy = line[0:5]
    saveMin = min(copy)
    if saveMin >= 0:
        return (-1, -1)
    xp , yp = copy.index(saveMin), -1
    saveMin = 9999999999
    for i in range(0, valY - 1):
        if (matrix[i][valX - 1]):
            if (matrix[i][xp] > 0 and (saveMin > matrix[i][valX - 1] / matrix[i][xp] and matrix[i][valX - 1] / matrix[i][xp] > 0)):
                yp = i
                saveMin = matrix[i][valX - 1] / matrix[i][xp]
        elif saveMin > matrix[i][xp] and matrix[i][xp] > 0:
            yp = i
            saveMin = matrix[i][valX - 1] / matrix[i][xp]
    return (yp, xp)

def usePivot(matrix, yp, xp):
    pivotPoint = matrix[yp][xp]
    for a in range(len(matrix[yp])):
        matrix[yp][a] = matrix[yp][a] / pivotPoint
    maxY, maxX = len(matrix), len(matrix[0])
    for i in range(maxY):
        if i == yp:
            continue
        val = matrix[i][xp]
        for j in range(maxX):
            matrix[i][j] -= val * matrix[yp][j]

def calc(matrix):
    order = [-1] * 4
    i = 0

    while 1:
        i += 1
        if i == 6:
            break
        yp, xp = findPivot(matrix)
        if (xp < 0 or yp < 0):
            break
        usePivot(matrix, yp, xp)
        order[yp] = xp
    return (order, matrix)

def finalPrint(nList, pList, resultOrder, total):
    print("Resources: %d F1, %d F2, %d F3, %d F4" %(nList[0], nList[1], nList[2], nList[3]))
    print("")
    print("Oat: %d units at $%d/unit" % (resultOrder[0], pList[0]) if resultOrder[0] == 0 else "Oat: %.2f units at $%d/unit" % (resultOrder[0], pList[0]))
    print("Wheat: %d units at $%d/unit" % (resultOrder[1], pList[1])  if resultOrder[1] == 0 else "Wheat: %.2f units at $%d/unit" % (resultOrder[1], pList[1]))
    print("Corn: %d units at $%d/unit" % (resultOrder[2], pList[2])  if resultOrder[2] == 0 else "Corn: %.2f units at $%d/unit" % (resultOrder[2], pList[2]))
    print("Barley: %d units at $%d/unit" % (resultOrder[3], pList[3])  if resultOrder[3] == 0 else "Barley: %.2f units at $%d/unit" % (resultOrder[3], pList[3]))
    print("Soy: %d units at $%d/unit" % (resultOrder[4], pList[4])  if resultOrder[4] == 0 else "Soy: %.2f units at $%d/unit" % (resultOrder[4], pList[4]))
    print("")
    print("Total production value: $%.2f" % total)

def algo(n1, n2, n3, n4, po, pw, pc, pb, ps):
    nList = [n1, n2, n3, n4]
    pList = [po, pw, pc, pb, ps]
    matrix = creatingMatrix(nList, pList)
    order = calc(matrix)[0]
    resultOrder = [0] * 5
    for i in [0, 1, 2, 3]:
        if order[i] != -1:
            resultOrder[order[i]] = matrix[i][len(matrix[i]) - 1]
    finalPrint(nList, pList, resultOrder, matrix[-1][-1])