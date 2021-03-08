##
## EPITECH PROJECT, 2020
## B-MAT-500-REN-5-1-305construction-eliott.palueau
## File description:
## main
##

import sys
from calc import *

# USAGE
#   ./305construction file
# DESCRIPTION
#   file    file describing the tasks


### Error management ###
def checkArguments():
	array = []

	if len(sys.argv) != 2:
		print("Invalid number of args")
		exit(84)
	try:
		with open(sys.argv[1], "r") as file:
			for line in file:
				array += line.split('\n')
	except IOError:
		print("Invalid file")
		exit (84)
	if len(array) == 0:
		print("Empty File")
		exit(84)
	array = filter(None, array)
	tmp = list()
	for each in array:
		tmp.append(each)
	return tmp


def checkFile(array):
	tmp = ""
	for line in array:
		if line[-1] == ';':
			print("Invalid line: line ending by \";\"")
			exit(84)
		if isNum(line) == False:
			print("Invalid line: no duration specified")
			exit(84)
		tmp = line.split(';')
		if len(tmp) < 3:
			print("Invalid line: not enough information")
			exit(84)

def isNum(str):
	return any(i.isdigit() for i in str)

def main():
	array = checkArguments()
	checkFile(array)
	engine(array);

