##
## EPITECH PROJECT, 2020
## 302separation
## File description:
## matrix
##


import sys
import math
from collections import OrderedDict

### Build the graph to facilitate all the following things ###
def buildGraph(array):
	allfile = list()
	graph = OrderedDict()
	names = []

	for connection in array:
		allfile.append(connection.rstrip())
		tmp = connection.rstrip()
		names += tmp.split(" is friends with ")
	names = list(dict.fromkeys(names))
	names = sorted(names)

	for name in names:
		graph[name] = ""

	for name in names:
		for string in allfile:
			tmp = string.split(" is friends with ")
			left = tmp[0]
			right = tmp[1]
			if (name == left):
				for x, y in graph.items():
					if (x == name):
						graph[left] += (right + ",")
						graph[right] += (left + ",")
	return graph

### Good display of the matrix ###
def dispMatrix(matrix, len):
	for y in range(len):
		for i in range(len - 1):
			sys.stdout.write(str(matrix[y][i]) + " ")
		sys.stdout.write(str(matrix[y][len - 1]) + "\n")

shortest = int(0)
### Recursive search ###
def recurSearch(stack, person, goal, graph, links):

	tmp = 0
	curr = 0
	global shortest
	friendsList = graph[person]
	friendsList = friendsList.split(',')
	friendsList.pop()
	if goal in friendsList:
		if shortest > links or shortest == 0:
			shortest = links
		return shortest

	for name in friendsList:
		if name in stack:
			continue
		stack.append(name)
		recurSearch(stack, name, goal, graph, links + 1)
		stack.pop()
	return tmp

### Finding shortest path to someone ###
def findingPeople(start, end, graph):
	stack = list()
	stack.append(start)
	global shortest
	shortest = 0
	if start == end:
		return 0
	recurSearch(stack, start, end, graph, 1)
	return shortest

### Filling matrixes using graph ###
def printMatrix(graph, array):
	i = 0
	j = 0
	savelen = 0
	matrix = list(list())
	names = []
	limit = int(sys.argv[2])

	for each in graph:
		i += 1
	for y in range(i):
		matrix.append(list())
		for x in range(i):
			matrix[y].append(0)
	savelen = i
	for connection in array:
		tmp = connection.rstrip()
		names += tmp.split(" is friends with ")
	names = list(dict.fromkeys(names))
	names = sorted(names)

	for x, y in graph.items():
		tmplist = y.split(',')
		for each in tmplist:
			if each == "":
				i = 0
			else :
				i = 0
				while i < savelen and names[i - 1] != each:
					i += 1
				matrix[j][i - 1] = 1
		j += 1
	dispMatrix(matrix, savelen)
	print

	i = 0
	j = 0
	for name in names:
		for i in range(savelen):
			tmp = findingPeople(name, names[i], graph)
			matrix[j][i] = tmp if tmp <= limit else 0
			i += 1
		i = 0
		j += 1

	dispMatrix(matrix, savelen)

### Engine for matrix display ###
def matrixEngine(array, names):

	if not sys.argv[2].isdigit():
		print("Invalid limit (number expected)")
		exit(84)

	for name in names:
		print(name)
	print("")
	graph = buildGraph(array)
	printMatrix(graph, array)