node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]


class Node:
    def __init__(self,date,left=None,right=None):
        self.date,self.left,self.right=date,left,right


class Tree:
    def __init__(self,root=None,):
        self.root=root
    def init_date(dates):
        node_dict={}
        for d in dates:
            node=Node(d["date"],d["left"],d["right"])
            node_dict[d["date"]]=node
        for d in dates:
            node=node_list[n["date"]]

            if node.left:
                node.left=node_dict[node.left]
            if node.right:
                node.right=node_dict[node.right]

if __name__ == "_main_":
    tree=Tree()
    tree.init_date()