def insertionSort(myList):
	for index in range(1, len(myList)):
		currentValue = myList[index]
		position = index
		while position > 0 and myList[position - 1] > currentValue:
			myList[position] = myList[position - 1]
			position = position - 1
		myList[position] = currentValue
	return myList

if __name__ == "__main__":
	list = [5,3,6,2,9,45,23,46]
	sorted = insertionSort(list)
	print(sorted)