def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        leftHalf = myList[:mid]
        rightHalf = myList[mid:]

        mergeSort(leftHalf)
        mergeSort(rightHalf)

        i=0;
        j=0;
        k=0;

        while i < len(leftHalf) and j < len(rightHalf):
            if leftHalf[i] < rightHalf[j]:
                myList[k] = leftHalf[i]
                i = i+1
            else:
                myList[k] = rightHalf[j]
                j=j+1
            k=k+1

        while i < len(leftHalf):
            myList[k] = leftHalf[i]
            i=i+1
            k=k+1

        while j < len(rightHalf):
            myList[k] = rightHalf[j]
            j=j+1
            k=k+1
    return myList

if __name__ == '__main__':
    list = [54,26,93,17,77,31,4,55,20]
    sorted = mergeSort(list)
    print(sorted)
