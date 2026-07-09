def bubble_sort(arr):
    # 获取数组长度
    n = len(arr)
    # 外层循环控制排序轮次
    for i in range(n):
        # 标记本轮是否发生交换，优化有序数组
        swapped = False
        # 内层循环比较相邻元素，每轮末尾i个元素已排好，无需遍历
        for j in range(0, n - i - 1):
            # 前一个比后一个大，交换位置
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # 本轮无交换，说明数组已经有序，直接退出循环
        if not swapped:
            break
    return arr


# 测试代码
if __name__ == "__main__":
    test_list = [8, 2, 5, 1, 9, 3, 7, 4, 6]
    print("原数组：", test_list)
    bubble_sort(test_list)
    print("排序后：", test_list)