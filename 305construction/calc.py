##
## EPITECH PROJECT, 2020
## B-MAT-500-REN-5-1-305construction-eliott.palueau
## File description:
## calc
##

import sys
import math
from collections import OrderedDict

def createLists(array):
    tasks = list()
    times = list()
    befores = list()
    i = 0

    for line in array:
        tmpList = line.split(';')
        if (int(tmpList[2]) < 0):
            exit(84)
        if (tmpList[0] in tasks):
            exit(84)
        tasks.append(tmpList[0])
        times.append(int(tmpList[2]))
        befores.append(list())
        for each in tmpList[3:]:
            befores[i].append(each)
        i += 1
    return tasks,times,befores

def checkFinishedTasks(tasks, times, befores, orders, j):
    i = 0
    length = len(times)

    while i < len(befores):
        if (times[i] == 0):
            k = 0
            l = 0
            while k < length:
                l = 0
                while l < len(befores[k]):
                    if befores[k][l] == tasks[i]:
                        befores[k].pop(l)
                    else:
                        l += 1
                k += 1
                orders[tasks[i]] = j
            tasks.pop(i)
            times.pop(i)
            befores.pop(i)
            length -= 1
            i -= 1
        i += 1
    return length

def printStartTime(tasks, times, befores, orders, duration):
    delay = list()
    tmp = 0

    for each in tasks:
        delay.append(0)
    for i in range(len(tasks)):
        tmp = duration
        for j in range(len(tasks)):
            if tasks[i] in befores[j] and tmp > orders[tasks[j]]:
                tmp = orders[tasks[j]]
        delay[i] = tmp - (orders[tasks[i]] + times[i])
    for task, time in orders.items():
        for i in range(len(times)):
            if task == tasks[i] and delay[i] > 0:
                print(task + " must begin between t=" + str(time) + " and t=" + str(time + delay[i]))
            elif task == tasks[i]:
                print(task + " must begin at t=" + str(time))
    return delay

def printFormat(tasks, times, befores, orders, duration):
    constLength = len(tasks)
    ends = list(orders.values())

    for i in range(len(times)):
        orders[tasks[i]] -= times[i]
    if (duration > 1):
        print("Total duration of construction: " + str(duration - 1) + " weeks")
    print("")
    delay = printStartTime(tasks, times, befores, orders, duration - 1)

    k = 0
    print("")
    for each, time in orders.items():
        i = 0
        sys.stdout.write(each + "\t(")
        for t in range(len(delay)):
            if each == tasks[t]:
                sys.stdout.write(str(delay[t]) + ")\t")
        while i < duration:
            if time == i:
                for each in range(ends[k] - time):
                    sys.stdout.write("=")
                    i += 1
                break;
            sys.stdout.write(" ")
            i += 1
        k += 1
        print("")

### Engine ###
def engine(array):
    tasks, times, befores = createLists(array)
    orders = OrderedDict()
    constLength = len(befores)
    length = constLength
    working = False
    i = 0
    duration = 0

    while len(orders) != constLength:
        i = 0
        length = checkFinishedTasks(tasks, times, befores, orders, duration)
        wprking = False
        while (i < length):
            if (len(befores) == 0):
                working = True
                break
            if (len(befores[i]) == 0):
                working = True
                times[i] -= 1
            i += 1
        if working == False:
            exit(84)
        duration += 1

    tasks, times, befores = createLists(array)
    printFormat(tasks, times, befores, orders, duration)
