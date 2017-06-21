def shellSort(myList):
	sublistCount = len(myList) // 2
	while sublistCount > 0:
		for startPosition in range(sublistCount):
			gapInsertionSort(myList, startPosition, sublistCount)
		sublistCount = sublistCount // 2
	return myList

def gapInsertionSort(myList, start, gap):
	for index in range(start + gap, len(myList), gap):
		currentValue = myList[index]
		position = index
		while position >= gap and myList[position - gap] > currentValue:
			myList[position] = myList[position - gap]
			position = position - gap
		myList[position] = currentValue

if __name__ == '__main__':
	list = [7,9,23,3,76,1,98,46,34,56,87]
	sorted = shellSort(list)
	print(sorted)