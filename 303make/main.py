##
## EPITECH PROJECT, 2020
## 303
## File description:
## main
##

import sys
from calc import *


# USAGE
# 		./303make makefile [file]
# DESCRIPTION
# 		makefile    name of the makefile
# 		file        name of a recently modified file


def checkArguments():
	array = []

	if len(sys.argv) != 2 and len(sys.argv) != 3:
		print("Invalid number of args")
		exit(84)
	try:
		with open(sys.argv[1], "r") as file:
			for line in file:
				array.append(line.split())
	except IOError:
		print("Invalid file")
		exit (84)
	if len(array) == 0:
		print("Empty File")
		exit(84)
	return array


def main():
	sys.setrecursionlimit(1500)
	array = checkArguments()
	if len(sys.argv) == 2:
		matrixEngine(array)
	else:
		clinesEngine(array, sys.argv[2])
