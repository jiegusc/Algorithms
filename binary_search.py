def binary_search(list, key):
    r = len(list) - 1
    l = 0
    time = 0
    while l <= r:
        time += 1
        mid = (r + l) // 2
        # mid = l + int((r - l) * (key - list[l]) // (list[r] - list[l]))
        if list[mid] == key:
            return mid, time
        elif list[mid] < key:
            l = mid + 1
        else:
            r = mid - 1
    return "not in the list",time


a = [1,20,30,46,54,66,73,84,96,107,113,128]
# a = [1,2,3,4,5,6,7,8,9]

k = 8

print(binary_search(a,k))
