def shell_sort(arr):
    # 获取数组长度
    n = len(arr)
    # 初始步长设为长度一半，每次除以2缩小步长
    gap = n // 2

    # 步长循环，gap=0时结束
    while gap > 0:
        # 分组插入排序
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # 同组向前比较交换
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        # 缩小步长
        gap = gap // 2
    return arr


# 测试
if __name__ == "__main__":
    nums = [8, 2, 5, 1, 9, 3, 7, 4, 6]
    shell_sort(nums)
    print("排序结果：", nums)