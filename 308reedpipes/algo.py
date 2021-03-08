##
## EPITECH PROJECT, 2021
## B-MAT-500-REN-5-1-308reedpipes-eliott.palueau
## File description:
## algo
##

def systemResolution(ordinate, abscissa):
    A = 6 * (ordinate[2] - 2 * ordinate[1] + ordinate[0]) / 50
    B = 6 * (ordinate[3] - 2 * ordinate[2] + ordinate[1]) / 50
    C = 6 * (ordinate[4] - 2 * ordinate[3] + ordinate[2]) / 50
    system = [0, 0, 0, 0, 0]

    system[2] = (B - (A + C) / 4) * 4 / 7
    system[1] = A / 2 - 0.25 * system[2]
    system[3] = C / 2 - 0.25 * system[2]
    return system

def f(ordinate, abscissa, system, x, j):
    result = (- system[j - 1] / 30 * pow(x - abscissa[j], 3) + system[j] / 30 * pow(x - abscissa[j - 1], 3) - (ordinate[j - 1] / 5 - 5 / 6 * system[j - 1]) * (x - abscissa[j]) + (ordinate[j] / 5 - 5 / 6 * system[j]) * (x - abscissa[j - 1]))
    return result

def computer(ordinate, abscissa, n):
    system = systemResolution(ordinate, abscissa)
    resultList = list()

    for i in range(n):
        x = 20 / (n - 1) * i
        j = int((x - 0.01) / 5) + 1
        resultList.append(f(ordinate, abscissa, system, x, j))
    return resultList

def algo(r0, r5, r10, r15, r20, n):
    abscissa = [0, 5, 10, 15, 20]
    ordinate = [r0, r5, r10, r15, r20]
    vector = systemResolution(ordinate, abscissa)
    result = computer(ordinate, abscissa, n)

    for i in range(len(vector)):
        vector[i] = round(vector[i], 1)
        if (vector[i] == -0.0):
            vector[i] = 0
    print("vector result: [%.1f, %.1f, %.1f, %.1f, %.1f]" %(vector[0], vector[1], vector[2], vector[3], vector[4]))

    for i in range(n):
        print("abscissa: %.1f cm\tradius: %.1f cm" %((20 / (n - 1) * i), result[i]))