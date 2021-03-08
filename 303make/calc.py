##
## EPITECH PROJECT, 2020
## 303
## File description:
## calc
##

import sys
import math
from collections import OrderedDict

### Build graph ###
def getFileList(array):
    fileList = dict()
    for line in array:
        if (len(line) > 0 and line[0][-1] == ':'):
            fileList[line[0][:-1]] = ""
            for i in line[1:]:
                fileList[i] = ""
    return sorted(fileList)

def findNameList(name, fileList):
    i = 0

    for k in range(len(fileList)):
        if fileList[k] == name:
            i = k
    return i

def amountOfPresence(name, array):
    count = 0

    for line in array:
        for words in line:
            if (len(line) > 0 and line[0][-1] == ':'):
                if words == name:
                    count += 1

    return count

def lastOne(graph, name):
    count = 0
    length = len(graph)

    for each in (graph.keys()):
        if each == name:
            break
        count += 1
    print("Count", count)
    print("Length", length)
    if count == length:
        return True
    else:
        return False

def recurGraph(graph, name, links):

    if len(graph[name]) == 0:
        sys.stdout.write(links)
        return
    links += name + " -> "
    for each in graph[name]:
        links += each
        if (len(graph[each]) > 0):
            links += " -> "
        recurGraph(graph, each, links)

def printFileArrow(array, fileList, fileLinks):
    target = ""
    atEnd = False
    links = str()
    count = 0
    saveArray = array

    for i in range(len(fileList)):
        if len(fileLinks[i]) == 0:
            continue
        sys.stdout.write(fileList[i] + " -> ")
        target = fileList[i]
        while 1:
            if len(fileLinks[findNameList(target, fileList)]) == 0:
                break
            for line in array:
                if (len(line) > 0 and line[0][-1] == ':'):
                    if target in line:
                        sys.stdout.write(line[0][:-1])
                        if len(fileLinks[findNameList(line[0][:-1], fileList)]) != 0:
                            sys.stdout.write(" -> ")
                        target = line[0][:-1]
                        break
        print("")

    # graph = OrderedDict()
    # for i in range(len(fileList)):
    #     graph[fileList[i]] = list()
    #     for each in fileLinks[i]:
    #         graph[fileList[i]].append(each)

    # for file, lists in graph.items():
    #     links = file + " -> "
    #     if len(lists) == 0:
    #         continue
    #     for each in lists:
    #         if len(graph[each]) == 0:
    #             sys.stdout.write(links  + each)
    #             if file != graph.keys()[-1]:
    #                 print("")
    #             continue
    #         recurGraph(graph, each, links)
    #         if file != graph.keys()[-1]:
    #             print("")
    # print("")

### Engine for Option 1 -> Matrice display ###
def matrixEngine(array):
    fileList = getFileList(array)
    fileLinks = list()
    matrix = list()
    i = 0
    count = 0

    for each in fileList:
        fileLinks.append(list())
        for line in array:
            if len(line) > 0 and line[0][-1] == ':' and each in line:
                fileLinks[i].append(line[0][:-1])
            fileLinks[i] = sorted(fileLinks[i])
        i += 1
    for i in range(len(fileList)):
        matrix.append(list())
        for j in range(len(fileList)):
            matrix[i].append(0)

    for i in range(len(fileList)):
        for name in fileLinks[i]:
            matrix[i][findNameList(name, fileList)] = 1
    for line in matrix:
        sys.stdout.write("[")
        for each in line[:-1]:
            sys.stdout.write(str(each) + " ")
        print(str(line[-1]) + "]")
        count += 1
    if count == 0:
        print("Inconsistent file")
        exit(84)
    print("")

    printFileArrow(array, fileList, fileLinks)


def printingCompileLine(fileList, fileLinks, array, file):
    i = 84
    target = ""

    if file == "":
        return
    for k in range(len(fileList)):
        if fileList[k] == file:
            i = k
    if i == 84:
        exit(84)
    for links in fileLinks[i]:
        target = links + ":"
        for k in range(len(array)):
            if len(array[k]) > 0 and array[k][0][-1] == ':' and target in array[k]:
                for listPart in array[k + 1:]:
                    if (len(listPart) == 0):
                        break
                    else:
                        for part in listPart:
                            sys.stdout.write(part)
                            if part != listPart[-1]:
                                sys.stdout.write(" ")
                        print("")
    if len(fileLinks[i]) == 0:
            exit(0)
    for links in fileLinks[i]:
        printingCompileLine(fileList, fileLinks, array, links)

### Engine for Option 2 -> Display 'cc' lines ###
def clinesEngine(array, file):
    fileList = getFileList(array)
    fileLinks = list(list())
    i = 0

    for each in fileList:
        fileLinks.append(list())
        for line in array:
            if len(line) > 0 and line[0][-1] == ':' and each in line:
                fileLinks[i].append(line[0][:-1])
            fileLinks[i] = sorted(fileLinks[i])
        i += 1
    if len(fileLinks[findNameList(file, fileList)]) == 0:
        print("")
        return(0)
    printingCompileLine(fileList, fileLinks, array, file)
