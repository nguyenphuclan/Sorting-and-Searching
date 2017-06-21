def bubleSort(myList):
	for numpass in range(len(myList) - 1, 0, -1):
		for i in range(numpass):
			if myList[i] > myList[i + 1]:
				temp = myList[i]
				myList[i] = myList[i + 1]
				myList[i + 1 ] = temp
	return myList

if __name__ == "__main__":
	list = [1, 13, 9 ,5, 45, 34, 14]
	sorted = bubleSort(list)
	print(sorted)