def merge_sorting(data):
    print(f"Splitting {data}")
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sorting(left)
        merge_sorting(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] > right[j]:
                data[k] = right[j]
                j += 1
            else:
                data[k] = left[i]
                i += 1
            k += 1

        while i < len(left):
            data[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            data[k] = right[j]
            j += 1
            k += 1
    print(f"Merging {data}")

alist = [54,26,93,17,77,31,44,55,20]
merge_sorting(alist)
print(alist)
# def mergeSort(alist):
#     print(f'Splitting{alist}')
#     if len(alist) > 1:
#         mid = len(alist) // 2
#         left = alist[:mid]
#         right = alist[mid:]
#         mergeSort(left)
#         mergeSort(right)
#
#         i = 0
#         j = 0
#         k = 0
#         while i < len(left) and j < len(right):
#             if left[i] > right[j]:
#                 alist[k] = right[j]
#                 j += 1
#             else:
#                 alist[k] = left[i]
#                 i += 1
#             k += 1
#         while i < len(left):
#             alist[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             alist[k] = right[j]
#             j += 1
#             k += 1
#     print(f"Merging {alist}")
#
#
# alist = [54,26,93,17,77,31,44,55,20]
# mergeSort(alist)
# print(alist)
