##
## EPITECH PROJECT, 2020
## 302separation
## File description:
## degree
##

import sys
import math

friends = list()
positions = list()
data = list()
checked = list()

### Is person already checked? ###
def isCheck(npos):
	global checked

	for i in range(len(checked)):
		if npos == checked[i]:
			return True
	return False

### Recursive func ###
def findLink(names, position, toFind, degree):
	global friends
	global data
	idx = friends[position]

	for i in range(len(idx)):
		if idx[i] == toFind:
			data.append(degree + 1)
	for i in range(len(idx)):
		npos = findPos(idx[i], names)
		if isCheck(npos) == False:
			checked.append(npos)
			findLink(names, npos, toFind, degree + 1)

### Find name position in names list ###
def findPos(toFind, names):
	count = 0

	for name in names:
		if toFind == name:
			return(count)
		count += 1
	return(-1)

### Return False if name is not in the list ###
def nameInList(toFind, names):
	for name in names:
		if name == toFind:
			return True
	return False

### Engine for degree separation ###
def degreeEngine(array, names, person1, person2):
	global positions
	global friends
	global data
	pos1 = 0
	connections = []
	left = []
	right = []

	if nameInList(person1, names) == False or nameInList(person2, names) == False:
		sys.stdout.write("Degree of separation between %s and %s: -1\n" %(person1, person2))
		exit(0)

	if person1 == person2:
		sys.stdout.write("Degree of separation between %s and %s: 0\n" %(person1, person2))

	pos1 = findPos(person1, names)
	positions.append(pos1)

	for connect in array:
		tmp = connect.rstrip()
		connections.append(tmp.split(" is friends with "))

	for connect in connections:
		left.append(connect[0])
		right.append(connect[1])

	for guy in names:
		tab = []
		for i in range(len(left)):
			if guy == left[i]:
				tab.append(right[i])
			if guy == right[i]:
				tab.append(left[i])
		friends.append(tab)
	findLink(names, pos1, person2, -1)
	if len(data) == 0:
		sys.stdout.write("Degree of separation between %s and %s: -1\n" %(person1, person2))
	else:
		tmp = data[0]
		for i in range(len(data)):
			if data[i] < tmp:
				tmp = data[i]
		if tmp == 0:
			tmp = 1
		sys.stdout.write("Degree of separation between %s and %s: %d\n" %(person1, person2, tmp))
