def countingSort(array, maxval):
    minval = min(array)
    m = maxval - minval + 1
    count = [0] * m               
    for a in array:
        count[a - minval] += 1             
    i = 0
    for a in range(m):            
        for c in range(count[a]): 
            array[i] = a + minval
            i += 1
    return array


if __name__ == '__main__':
    list = [6,4,7,2, 12 ,1,3, 100, 45]
    sorted = countingSort(list, max(list))
    print(sorted)