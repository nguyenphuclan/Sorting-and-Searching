def binary(myItem, mylist):
	bot = 0
	top = len(mylist) - 1
	found = False
	while bot <= top and not found:
		middle = (bot + top) // 2
		if mylist[middle] == myItem:
			found = True
		elif mylist[middle] < myItem:
			bot = middle + 1
		else:
			top = middle -1
	return found

if __name__ == "__main__":
	numberList = [2, 5, 7, 9, 34, 76, 91, 186, 868]
	item = int(input("Hay nhap so ban muon tim: "))
	isFound = binary(item, numberList)
	if isFound:
		print("So cua ban co trong danh sach")
	else:
		print("So cua ban ko co trong ds")