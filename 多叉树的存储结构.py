class TreeNode:
    def __init__(self, value):
        self.value = value              # 节点存储的值
        self.first_child = None        # 指针：指向【第一个子节点】
        self.right_sibling = None      # 指针：指向【右边的兄弟节点】
# ==============================================
# 2. 定义【二叉树】节点类
# 标准二叉树结构：左孩子、右孩子
# ==============================================
class BinaryTree:
    def __init__(self, value):
        self.value = value             # 节点存储的值
        self.left = None               # 二叉树左孩子
        self.right = None              # 二叉树右孩子

def convert_binary_to_tree(binary_tree):
    # 递归终止条件：如果节点为空，返回 None
    if not binary_tree:
        return None
    # 1. 根据二叉树节点的值，创建对应的【普通树节点】
    root = TreeNode(binary_tree.value)
    # 2. 二叉树的【左子树】 = 普通树的【第一个孩子】
    root.first_child = convert_binary_to_tree(binary_tree.left)
    # 3. 二叉树的【右子树】 = 普通树的【右兄弟】
    root.right_sibling = convert_binary_to_tree(binary_tree.right)
    # 返回转换好的普通树节点
    return root

def convert_binary_to_forest(binary_tree):
    # 如果二叉树为空，返回空森林
    if not binary_tree:
        return []
    forest = []        # 用列表存储森林中的所有树
    current = binary_tree  # 从根节点开始遍历
    # 沿着【右链】一直走，每遇到一个节点就是一棵树的根
    while current:
        # 1. 创建当前树的根节点
        tree = TreeNode(current.value)
        # 2. 根的左子树 → 这棵树的孩子结构
        tree.first_child = convert_binary_to_tree(current.left)
        # 3. 把这棵树加入森林
        forest.append(tree)
        # 4. 继续向右走，取下一棵树的根
        current = current.right
    # 返回整个森林
    return forest

def print_tree(root):
    if root:
        print(root.value, end=" ")      # 先访问根节点
        # 从第一个孩子开始，遍历所有兄弟
        child = root.first_child
        while child:
            print_tree(child)           # 递归遍历子树
            child = child.right_sibling # 兄弟节点依次遍历
def print_forest(forest):
    for tree in forest:
        print_tree(tree)  # 打印每一棵树
        print()          # 树与树之间换行分隔
if __name__ == "__main__":
    # ----------------------
    # 步骤1：手动构建一棵二叉树
    # 结构如下：
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    # ----------------------
    binary_tree = BinaryTree(1)
    binary_tree.left = BinaryTree(2)
    binary_tree.right = BinaryTree(3)
    binary_tree.left.left = BinaryTree(4)
    binary_tree.left.right = BinaryTree(5)
    binary_tree.right.right = BinaryTree(6)
    # ----------------------
    # 步骤2：执行转换
    # ----------------------
    # 二叉树 → 普通树
    tree = convert_binary_to_tree(binary_tree)
    # 二叉树 → 森林
    forest = convert_binary_to_forest(binary_tree)
    # ----------------------
    # 步骤3：输出结果
    # ----------------------
    print("二叉树 转换为 普通树（前序遍历）：")
    print_tree(tree)
    print("\n---------------------")
    print("二叉树 转换为 森林（每棵树前序遍历）：")
    print_forest(forest)