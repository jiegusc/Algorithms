def select_sorting(arr):
    for i in range(len(arr)):
        min_temp = arr[i]
        min_index = i
        for j in range(i, len(arr)):
            if arr[j] < min_temp:
                min_temp = arr[j]
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


a = [30,50,57,77,62,78,94,80,84]
print(select_sorting(a))

# 选择一个最小的元素并依次放入数组
