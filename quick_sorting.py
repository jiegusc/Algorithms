def partition(arr, low, high):
    i = (low - 1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            # current index of the item which are small than pivot
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        sort(arr, low, p - 1)
        sort(arr, p+ 1, high)
    return arr

a = [10, 7, 8, 9, 1,1, 21,  5]

print(sort(a, 0, len(a) - 1))

# 先选择最后一个为pivot，小于这个值得都放在左边，顺序无所谓。接下来再用sort递归左边和右边