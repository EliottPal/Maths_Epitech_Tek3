##
## EPITECH PROJECT, 2020
## 306radiator
## File description:
## algo
##

h = 0.5
import numpy as np
import math

def math_round(n, decimals=0):
    n *= 10**decimals
    n = math.floor(n) if n - math.floor(n) < 0.5 else math.ceil(n)
    return n / 10**decimals


def buildIdentityMatrix(n):
    A = list()

    for y in range(n * n):
        A.append(list())
        for x in range(n * n):
            if (x == y):
                A[y].append(1)
            else:
                A[y].append(0)

    for k in range(n * n):
        # Not in the first line and not in the first column and not in the last column and not in the last line
        if k > n and k % n != 0 and (k + 1) % n != 0 and k < (n * n - n):
            A[k][k] = -16
            A[k][k + 1] = 4
            A[k][k - 1] = 4
            A[k][k + n] = 4
            A[k][k - n] = 4
    return np.array(A)

def buildRadiatorMatrix(n, ir, jr):
    B = list()

    for y in range(n * n):
        B.append(0)
    B[n * jr + ir] = -300
    return np.array(B)

def findXMatrix(n, ir, jr, doWePrint):
    A = buildIdentityMatrix(n)
    B = buildRadiatorMatrix(n, ir, jr)
    size = n * n
    InvA = np.linalg.inv(A)

    if doWePrint:
        for line in A:
            for i in range(size):
                if i != size - 1:
                    print(str(line[i]) + "\t", end='')
                else:
                    print("" + str(line[i]), end='')
            print("")
        print("")


    X = np.matmul(InvA, B)
    if doWePrint:
        for each in X:
            if round(each, 1) == -0.0:
                print(0.0)
            else:
                print('%.1f' % math_round(each, 1))
    return X

def temperatureAtIJ(X, n, i, j):
    print(round(X[n * j + i], 1))