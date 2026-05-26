class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal(node):
    if node is None:
        return

    # 递归遍历左子树
    inorder_traversal(node.left)

    # 访问根节点
    print(node.value)

    # 递归遍历右子树
    inorder_traversal(node.right)


# 创建二叉树
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# 中序遍历二叉树
inorder_traversal(root)