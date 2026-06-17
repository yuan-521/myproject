def directIndexSort(arr):
    for i in range(1, len(arr)):
        m = i - 1
        t = arr[i]
        while m >= 0 and t < arr[m]:
            arr[m + 1] = arr[m]
            m = m - 1
        arr[m + 1] = t
    return arr

arr = [33, 17, 24, 71, 23, 55]
arr1 = directIndexSort(arr)
print(arr1)