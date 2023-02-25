def merge_sorting(data):
    print(f'Splitting {data}')
    if len(data) > 1:
        mid = len(data) // 2
        left = data[:mid]
        right = data[mid:]

        merge_sorting(left)
        merge_sorting(right)

        i = 0
        j = 0
        # index of the data in each call.
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
# merge_sorting(alist)
# print(alist)
import copy

# low, mid, high is the index of the array

def merge_(arr, low, mid, high):
    arr_ = copy.deepcopy(arr)
    m = mid + 1
    l = low

    for i in range(l, high + 1):
        #  == mid 时，也是由low来做处理
        if(l > mid):
            arr[i] = arr_[m]
            m += 1
        # 同理，这时的high 由m来做处理
        elif(m > high):
            arr[i] = arr_[l]
            l += 1
        elif(arr_[l] > arr_[m]):
            arr[i] = arr_[m]
            m += 1
        else:
            arr[i] = arr_[l]
            l += 1
    return


def sort_(arr, low, high):
    if(low >= high):
        return
    mid = (low + high) // 2
    sort_(arr, low, mid)
    sort_(arr, mid + 1, high)
    merge_(arr, low, mid, high)
    return

# sort_(alist, 0, len(alist) - 1)
merge_sorting(alist)
print(alist)

# 先算出中间值，并将数组分为2部分并分别去计算，之后在进行归并。