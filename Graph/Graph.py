from queue import Queue
from Operator import Operator


class Graph(Operator):
    def __init__(self, ring, type):
        self.ring = ring
        self.type = type

    def getNumber(self):
        return super().getNumber()

    def vertecies(self):
        return [x for x in range(self.getNumber()) if self.isVertex(x)]

    def edges(self):
        edge = [{x, y} for x in self.vertecies()
                for y in self.vertecies() if self.isEdge(x, y) and x < y]
        return self.clearDuplicate(edge)

    def notEdges(self):
        return self.clearDuplicate([{x, y} for x in self.vertecies() for y in self.vertecies() if not self.isEdge(x, y) and x < y])

    def isVertex(self, x):
        if self.type == 'annihilator':
            return x in self.zeroDivisor()
        elif self.type == 'unit':
            return x in self.elememt()
        elif self.type == 'zero divisor':
            return x in self.zeroDivisor()
        else:
            return "kami tidak mengenali jenis graf yang anda masukkan"

    def isEdge(self, x, y):
        if self.type == 'annihilator':
            return self.union(self.ann(x), self.ann(y)) != self.ann(x*y)
        elif self.type == 'unit':
            return x+y in self.unit(self.ring)

    def orde(self):
        return len(self.vertecies())

    def size(self):
        return len(self.edges())

    def neighboor(self, x):
        return [v for v in self.vertecies() if self.isEdge(v, x)]

    def structurGraph(self):
        res = dict()
        for v in self.vertecies():
            res[v] = self.neighboor(v)
        return res

    def degree(self, v):
        return len(self.neighboor(v))

    def degree_ve(self, v):
        neighboor = self.neighboor(v)
        temp = []
        for i in neighboor:
            temp.extend(self.neighboor(v))
        return len(self.clearDuplicate(temp))

    def path(self, v1, v2):
        visited = set()
        queue = Queue()

        queue.put(v1)
        visited.add(v1)

        parent = dict()
        parent[v1] = None

        temp = False
        while not queue.empty():
            node = queue.get()
            if node == v2:
                temp = True
                break

            for v in self.structurGraph():
                if v not in visited:
                    queue.put(v)
                    parent[v] = node
                    visited.add(node)
        res = []
        if temp:
            res.append(v2)
            while parent[v2] is not None:
                res.append(parent[v2])
                v2 = parent[v2]
            res.reverse()
        return res

    def distance(self, v1, v2):
        return len(self.path(v1, v2))-1

    def isMatching(self, e1, e2):
        return e1 != e2

    def matching(self):
        return [[i, j] for i in self.edges() for j in self.edges() if self.isMatching(i, j)]

    def matrixAdjancency(self):
        matrix = []
        for i in self.vertecies():
            row = []
            for j in self.vertecies():
                el = 1 if self.isEdge(i, j) else 0
                row.append(el)
            matrix.append(row)
        return matrix

    def seqDegree(self, type):
        if type == 'vertex':
            return list(map(self.degree, self.vertecies()))
        elif type == 'edge':
            return list(map(lambda y: list(map(self.degree, y)), self.edges()))
        elif type == 'not edge':
            return list(map(lambda y: list(map(self.degree, y)), self.notEdges()))
        else:
            return None


# TODO: melengkapi data jenis-jenis graf

# graph = Graph('Z_21','annihilator')

# for i in graph.elememt():
#     print(i,'->',graph.ann(i))