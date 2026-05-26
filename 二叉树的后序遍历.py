# 定义二叉树节点类
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# 后序遍历函数：左子树 → 右子树 → 根节点
def postorder_traversal(node):
    # 递归终止条件：节点为空时直接返回
    if node is None:
        return

    # 1. 递归遍历左子树
    postorder_traversal(node.left)
    # 2. 递归遍历右子树
    postorder_traversal(node.right)
    # 3. 访问根节点
    print(node.value, end=" ")


# 构建示例二叉树
def build_example_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


# 主程序
if __name__ == "__main__":
    tree_root = build_example_tree()
    print("后序遍历结果：")
    postorder_traversal(tree_root)