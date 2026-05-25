# 定义普通多叉树节点类（一个节点可以有多个子节点）
class TreeNode:
    # 构造方法：初始化节点值和子节点列表
    def __init__(self, value):
        # 节点存储的数据/值
        self.value = value
        # 子节点列表，用于存放所有子节点对象
        self.children = []
    # 添加子节点方法：将传入的节点添加到当前节点的子节点列表中
    def add_child(self, child):
        self.children.append(child)
    # 自定义对象打印格式，方便调试查看节点
    def __repr__(self):
        return f"TreeNode({self.value})"
    # 按层级缩进打印整棵树，直观展示树结构
    def print_tree(self):
        # 定义内部递归辅助函数：按层级打印单个节点
        # node：当前要打印的节点
        # level：当前所在层级，用于控制缩进
        def print_node(node, level=0):
            # 根据层级生成缩进，层级越深缩进越多，- 表示节点标识
            print("  " * level + f"- {node.value}")
            # 递归遍历当前节点所有子节点，层级+1
            for child in node.children:
                print_node(child, level + 1)
        # 从调用该方法的当前节点开始打印整棵树
        print_node(self)
# 根据列表格式的数据自动构建多叉树
def build_tree_from_list(lst):
    # 字典：key=节点值，value=节点对象，用于快速查找，避免重复创建节点
    node_map = {}
    # 树的根节点，初始为空
    root = None
    # 第一次遍历：创建所有节点，并建立父子关系
    for item in lst:
        # 获取当前节点的值
        value = item["value"]
        # 如果该值对应的节点还没创建，则新建节点并存入字典
        if value not in node_map:
            node_map[value] = TreeNode(value)
        # 取出当前节点对象
        node = node_map[value]
        # 第一个遍历到的节点作为整棵树的根节点
        if root is None:
            root = node
        # 获取当前节点的子节点值列表，没有children则返回空列表
        children_values = item.get("children", [])
        # 遍历每个子节点值
        for child_value in children_values:
            # 如果子节点不存在，则新建
            if child_value not in node_map:
                child_node = TreeNode(child_value)
                node_map[child_value] = child_node
            else:
                # 子节点已存在，直接从字典取出
                child_node = node_map[child_value]
            # 将子节点添加到当前节点的子节点列表
            node.add_child(child_node)
    # 返回构建完成的树根节点
    return root
# 程序入口，测试代码
if __name__ == "__main__":
    # 用列表定义树结构，每个字典代表一个节点：value=节点值，children=子节点值列表
    tree_data = [
        {"value": 1, "children": [2, 3, 4]},   # 根节点1，子节点2、3、4
        {"value": 2, "children": [5, 6]},       # 节点2，子节点5、6
        {"value": 3},                           # 节点3，无孩子
        {"value": 4, "children": [7, 8]},       # 节点4，子节点7、8
        {"value": 5},                           # 节点5，无孩子
        {"value": 6, "children": [9]},          # 节点6，子节点9
        {"value": 7},                           # 节点7，无孩子
        {"value": 8},                           # 节点8，无孩子
        {"value": 9}                            # 节点9，无孩子
    ]

    # 调用函数构建树
    root = build_tree_from_list(tree_data)
    # 调用打印方法，层级展示树结构
    root.print_tree()

