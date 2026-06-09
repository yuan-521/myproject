def block_search(blocks, values, target):
    """
    分块查找函数
    参数:
    - blocks: 块索引列表(存储每个块的最大值)
    - values: 已分块的有序数据列表
    - target: 要查找的目标值
    返回值:
    - 如果目标值在列表中,则返回其索引,否则返回-1
    """
    
    block_size = len(values) // len(blocks)
    
    for i in range(len(blocks)):
        start = i * block_size
        end = start + block_size
        # 判断目标值是否在当前块内
        if values[start] <= target <= values[end-1]:
            # 在块内进行顺序查找
            for j in range(start, end):
                if values[j] == target:
                    return j  
    return -1  

blocks = [0, 1, 2, 3, 4]  # 块索引列表
values = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]  # 数据列表
target = 16
result = block_search(blocks, values, target)
if result != -1:
    print(f"目标值 {target} 在索引位置 {result}")
else:
    print("目标值不存在")