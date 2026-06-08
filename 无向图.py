# 用字典实现邻接表表示图
class Graph:
    def __init__(self):
        # 存储图：键=顶点，值=该顶点相邻的顶点列表
        self.graph = {}

    # 添加顶点
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # 添加边（无向图：双向关联）
    def add_edge(self, v1, v2):
        # 先保证顶点存在
        self.add_vertex(v1)
        self.add_vertex(v2)
        # 互相加入邻接列表
        self.graph[v1].append(v2)
        self.graph[v2].append(v1)

    # 深度优先遍历 DFS
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()  # 记录已访问顶点
        # 当前顶点标记为已访问并输出
        visited.add(start)
        print(start, end=" ")

        # 递归遍历所有相邻顶点
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # 广度优先遍历 BFS（借助队列）
    def bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            # 取出队首元素
            current = queue.pop(0)
            print(current, end=" ")

            # 相邻顶点入队
            for neighbor in self.graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

# ========== 测试代码 ==========
if __name__ == "__main__":
    g = Graph()
    # 添加边构建图
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")
    g.add_edge("C", "D")
    g.add_edge("C", "E")

    print("邻接表结构：", g.graph)
    print("\n深度优先遍历 DFS：")
    g.dfs("A")

    print("\n\n广度优先遍历 BFS：")
    g.bfs("A")