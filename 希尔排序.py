def shellSort(arr):
    d = len(arr) // 2
    while d > 0:
        for i in range(d, len(arr)):
            t = arr[i]
            j = i
            while j >= d and arr[j - d] > t:
                arr[j] = arr[j - d]
                j = j - d
            arr[j] = t
        d //= 2
    return arr

arr = [33, 17, 24, 71, 23, 55, 16, 40, 37, 10, 32, 44]
arr1 = shellSort(arr)
print(arr1)