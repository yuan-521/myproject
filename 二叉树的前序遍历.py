class Node:
    def __init__(self, value):#value 自己存的值
        self.value = value   #将存进来的value存下
        self.left = None
        self.right = None

def preorder_traversal(node):
    if node is None:
        return

    # 先访问根节点
    print(node.value)   #前序遍历的第一步

    # 递归遍历左子树
    preorder_traversal(node.left)

    # 递归遍历右子树
    preorder_traversal(node.right)

# 创建二叉树
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# 前序遍历二叉树
preorder_traversal(root)      #调用函数