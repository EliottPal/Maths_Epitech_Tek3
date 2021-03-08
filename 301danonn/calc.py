##
## EPITECH PROJECT, 2020
## 301Dannon
## File description:
## calc
##

import sys
import math

mergeCount = int (0)

####### Count number of elements ######
def countElems(numbersArray):
	totalWords = 0

	for i in numbersArray:
		totalWords += 1

	if totalWords == 1:
		sys.stdout.write("1 element\n")
	else :
		sys.stdout.write("%d elements\n" %totalWords)

###### Convert string array into float array for calc + exit if file as not only numbers######
def convert(array):
	tab = list()

	for i in array:
		try:
			if float (i) or float(i).is_integer():
				tab.append(float(i))
		except ValueError:
			pass

	if len(tab) == 0:
		print("Invalid file")
		exit (84)

	return(tab)

###### Print result phrase without 's' if there is 0 or 1 comparisons ######
def printResult(nbr):
	if nbr == 1:
		sys.stdout.write("%d comparison\n" %nbr)
	else:
		sys.stdout.write("%d comparisons\n" %nbr)

###
####### Algorithms ######
###
def selectionSort(numbers):
	count = 0
	tab = numbers [:]

	for i in range(len(tab)):
		index = i
		for j in range(i + 1, len(tab)):
			count += 1
			if tab[index] >= tab[j]:
				index = j
		tab[i], tab[index] = tab[index], tab[i]

	sys.stdout.write("Selection sort: ")
	printResult(count)

def insertionSort(numbers):
	count = 0
	tab = numbers [:]

	for i in range(1, len(tab)):
		j = i
		while j > 0:
			count += 1
			if tab[j - 1] <= tab[j]:
				tab[j], tab[j - 1] = tab[j - 1], tab[j]
				j -= 1
			else:
				break

	sys.stdout.write("Insertion sort: ")
	printResult(count)

def bubbleSort(numbers):
	count = 0
	tab = numbers [:]
	length = len(tab)

	for i in range(length - 1):
		for j in range(0, length - 1 - i):
			count += 1
			if tab[j] > tab[j + 1] :
				tab[j], tab[j + 1] = tab[j + 1], tab[j]

	sys.stdout.write("Bubble sort: ")
	printResult(count)


def quickSortFunc(numbers):
	count = 0
	tab = numbers [:]
	length = len(tab)

	if length <= 1:
		return tab, count

	pivot = tab[0]
	left = list()
	right = list()
	equal = [pivot]

	for i in range(1, length):
		count += 1
		if tab[i] >= pivot:
			left.append(tab[i])
		else:
			right.append(tab[i])
	left = quickSortFunc(left)
	right = quickSortFunc(right)
	tab = left[0] + equal + right[0]
	count += left[1] + right[1]
	return tab, count

def quickSort(numbers):
	count = quickSortFunc(numbers)[1]

	sys.stdout.write("Quicksort: ")
	printResult(count)

def mergeSort(numbers):
	global mergeCount

	if len(numbers) > 1:
		m = len(numbers) // 2
		leftHalf = numbers[:m]
		rightHalf = numbers[m:]
		leftHalf = mergeSort(leftHalf)
		rightHalf = mergeSort(rightHalf)

		numbers =[]

		while len(leftHalf) > 0 and len(rightHalf) > 0:
			if leftHalf[0] < rightHalf[0]:
				mergeCount += 1
				numbers.append(leftHalf[0])
				leftHalf.pop(0)
			else:
				mergeCount += 1
				numbers.append(rightHalf[0])
				rightHalf.pop(0)

		for i in leftHalf:
			numbers.append(i)
		for i in rightHalf:
			numbers.append(i)

	return numbers

####### Engine ######
def calcEngine(filepath, array):
	countElems(array)
	numbers = convert(array)

	selectionSort(numbers)
	insertionSort(numbers)
	bubbleSort(numbers)
	quickSort(numbers)
	mergeSort(numbers)
	sys.stdout.write("Merge sort: ")
	printResult(mergeCount)

