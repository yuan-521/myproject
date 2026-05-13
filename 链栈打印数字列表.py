# 定义链栈节点
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# 定义链栈类
class LinkStack:
    def __init__(self):
        self.top = None  # 栈顶指针

    # 入栈操作
    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    # 出栈操作
    def pop(self):
        if self.top is None:
            return None
        item = self.top.data
        self.top = self.top.next
        return item

# 题目要求的操作流程
if __name__ == "__main__":
    stack = LinkStack()
    output = []

    # 输入序列：1 2 3 4 5 6，目标出栈序列：1 3 5 4 2 6
    stack.push(1)
    output.append(stack.pop())  # 1 出栈

    stack.push(2)
    stack.push(3)
    output.append(stack.pop())  # 3 出栈

    stack.push(4)
    stack.push(5)
    output.append(stack.pop())  # 5 出栈
    output.append(stack.pop())  # 4 出栈
    output.append(stack.pop())  # 2 出栈

    stack.push(6)
    output.append(stack.pop())  # 6 出栈

    # 输出结果
    print("".join(map(str, output)))