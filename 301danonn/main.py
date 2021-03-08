##
## EPITECH PROJECT, 2020
## 301Dannon
## File description:
## main
##

import sys
from calc import *

#USAGE
# 	./301dannon file
#DESCRIPTION
# 	file    file that contains the numbers to be sorted, separated by spaces

# https://intra.epitech.eu/module/2020/B-MAT-500/REN-5-1/acti-413110/project/file/B-MAT-500_301dannon.pdf

def checkArguments():
	words = []

	if len(sys.argv) != 2:
		print("Invalid number of args")
		exit(84)
	try:
		with open(sys.argv[1], "r") as file:
			for line in file:
				words += line.split()
	except IOError:
		print("Invalid file")
		exit (84)
	if len(words) == 0:
		print("Empty file")
		exit (84)

	return words


def main():
	sys.setrecursionlimit(1500)
	array = checkArguments()
	calcEngine(sys.argv[1], array)