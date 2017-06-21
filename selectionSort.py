def selectionSort(myList):
	for fillslot in range(len(myList) - 1,0,-1):
		posMax = 0
		for location in range(1,fillslot+1):
			if myList[location] > myList[posMax]:
				posMax = location
		temp = myList[fillslot]
		myList[fillslot] = myList[posMax]
		myList[posMax] = temp
	return myList

if __name__ == "__main__":
	list = [15,8,3,2,1,9,35,14]
	sorted = selectionSort(list)
	print(sorted)