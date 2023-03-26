def insert_sorting(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr

a = [30,50,57,77,62,78,94,80,84]
print(insert_sorting(a))

# 依次查找元素，并将元素与之前一个做比较，小的往前移动，直到index为1