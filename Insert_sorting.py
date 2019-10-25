def binary_search(list,key):
    length = len(list)
    low = 0
    heigth = length -1
    time = 0
    while low <= heigth:
        time += 1
        mid = low + int((heigth - low) * (key - list[low])/(list[heigth] - list[low]))
        if key > list[mid]:
            low = mid + 1
        elif key <list[mid]:
            heigth = mid - 1
        else:
            print("times: %s" % time)
            return mid

# if __name__ =='__main__':
#     LIST = [1, 5, 7, 8, 22, 54, 99, 123, 200, 222, 444]
#     result = binary_search(LIST, 444)
#     print(result)
#

def binary_search2(list, key):
    r = len(list) - 1
    l = 0
    time = 0
    while l <= r:
        time += 1
        # mid = (r + l) // 2
        mid = l + int((r - l) * (key - list[l]) / (list[r] - list[l]))
        if list[mid] == key:
            return mid, time
        elif list[mid] < key:
            l = mid + 1
        else:
            r = mid
    return "not in the list",time


# a = [1,20,30,46,54,66,73,84,96,107,113,128]
a = [1,2,3,4,5,6,7,8,9]

k = 8

print(binary_search2(a,k))
