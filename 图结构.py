class Vertex:
    def __init__(self, key):
        self.id = key

    def __hash__(self):
        return hash(self.id)

    def getId(self):
        return self.id


class Graph:
    def __init__(self):
        self.vexList = {}
        self.adjMatrix = {}
        self.vexNum = 0
        self.edgeNum = 0

    def addVertex(self, key):
        self.vexNum = self.vexNum + 1
        newVertex = Vertex(key)
        self.vexList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vexList:
            return self.vexList[n]
        else:
            return None

    def getVertices(self):
        return self.vexList.keys()

    def addEdge(self, u, v, weight=0):
        if u not in self.vexList:
            self.addVertex(u)
        if v not in self.vexList:
            self.addVertex(v)
        if u not in self.adjMatrix.keys():
            self.adjMatrix[u] = {}
        self.adjMatrix[u][v] = weight
        self.edgeNum = self.edgeNum + 1


if __name__ == '__main__':
    g = Graph()
    for i in range(7):
        g.addVertex(i)

    g.addEdge(0, 1, 1)
    g.addEdge(0, 4, 1)
    g.addEdge(1, 2, 1)
    g.addEdge(1, 3, 1)
    g.addEdge(2, 4, 1)
    g.addEdge(2, 5, 1)
    g.addEdge(3, 6, 1)
    g.addEdge(4, 5, 1)
    g.addEdge(5, 6, 1)

    for v in g.vexList.keys():
        if v in g.adjMatrix.keys():
            for w in g.adjMatrix[v].keys():
                print("( %s --- %s, weight=%s)" % (v, w, g.adjMatrix[v][w]))