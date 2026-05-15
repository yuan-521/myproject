class CircularQueue:
    """
    顺序存储 循环队列
    约定：
    1. front 指向队头元素位置
    2. rear  指向队尾元素的下一个空位
    3. 牺牲一个空位，区分队列空和队列满
    """
    def __init__(self, max_size=6):
        # 队列最大存储空间
        self.max_size = max_size
        # 初始化数组作为队列底层容器
        self.queue = [None] * self.max_size
        # 队头指针，初始为0
        self.front = 0
        # 队尾指针，初始为0
        self.rear = 0
    def is_empty(self):
        """判断队列是否为空"""
        # 队头指针 == 队尾指针 即为空
        return self.front == self.rear
    def is_full(self):
        """判断队列是否已满"""
        # 循环队列满的标准公式：(rear+1)对max_size取模 等于 front
        return (self.rear + 1) % self.max_size == self.front
    def en_queue(self, val):
        """入队操作：元素从队尾加入"""
        # 先判断是否已满，满了不能入队
        if self.is_full():
            print("队列已满，无法入队")
            return False
        # 把元素放入rear指向的位置
        self.queue[self.rear] = val
        # 队尾指针向后循环移动一位
        self.rear = (self.rear + 1) % self.max_size
        return True
    def de_queue(self):
        """出队操作：删除并返回队头元素"""
        # 判断是否为空，空队列不能出队
        if self.is_empty():
            print("队列为空，无法出队")
            return None
        # 取出队头元素
        val = self.queue[self.front]
        # 队头指针向后循环移动一位
        self.front = (self.front + 1) % self.max_size
        return val
    def get_front(self):
        """只获取队头元素，不出队、不改变指针"""
        if self.is_empty():
            print("队列为空")
            return None
        # 返回front指向的队头数据
        return self.queue[self.front]
    def size(self):
        """计算当前队列中实际元素个数"""
        # 循环队列元素个数标准公式
        return (self.rear - self.front + self.max_size) % self.max_size
    def show_queue(self):
        """遍历并打印当前队列所有元素"""
        if self.is_empty():
            print("队列为空")
            return
        print("队列元素：", end=' ')
        # 从队头开始遍历
        idx = self.front
        # 循环到队尾指针结束
        while idx != self.rear:
            print(self.queue[idx], end=' ')
            # 下标循环后移
            idx = (idx + 1) % self.max_size
        print()
# 测试主程序
if __name__ == "__main__":
    # 创建最大容量为6的循环队列
    # 实际最多存放 5 个元素（牺牲一个空位）
    cq = CircularQueue(6)
    # 依次入队 10 20 30 40
    cq.en_queue(10)
    cq.en_queue(20)
    cq.en_queue(30)
    cq.en_queue(40)
    # 打印队列所有元素
    cq.show_queue()
    # 输出当前队列元素个数
    print("当前元素个数：", cq.size())
    # 读取队头元素
    print("队头元素：", cq.get_front())
    # 队头元素出队
    print("出队元素：", cq.de_queue())
    # 出队后再次打印队列
    cq.show_queue()
    # 继续入队，测试循环复用数组空间
    cq.en_queue(50)
    cq.en_queue(60)
    cq.show_queue()