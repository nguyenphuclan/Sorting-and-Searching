def radix_sort(myList):
    modulus = 10
    div = 1
    while True:
        # empty array, [[] for i in range(10)]
        save_list = [[], [], [], [], [], [], [], [], [], []]
        for value in myList:
            least_digit = value % modulus
            least_digit = least_digit // div
            save_list[least_digit].append(value)
        modulus = modulus * 10
        div = div * 10

        if len(save_list[0]) == len(myList):
            return save_list[0]

        i =0
        for x in save_list:
            for y in x:
                myList[i] = y
                i = i + 1


if __name__ == '__main__':
    list = [13, 8, 1992, 31, 3, 1993, 45, 23]
    sorted = radix_sort(list)
    print(sorted)