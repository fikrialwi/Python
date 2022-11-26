from queue import Queue
from Algebra import Algebra


class Graph(Algebra):
    def __init__(self, ring, type):
        self.ring = ring
        self.type = type

    def getNumber(self):
        return super().getNumber()

    def vertecies(self):
        return [(x,y) for x in self.element() for y in self.element() if self.isVertex([x,y])] if self.type =="clean" else [x for x in range(self.getNumber()) if self.isVertex(x)]

    def edges(self):
        edge = [{x, y} for x in self.vertecies() for y in self.vertecies() if self.isEdge(x, y) and x!= y]
        return self.clearDuplicate(edge)

    def notEdges(self):
        return self.clearDuplicate([{x, y} for x in self.vertecies() for y in self.vertecies() if not self.isEdge(x, y) and x < y])

    def isVertex(self, x):
        if self.type == 'annihilator':
            return x in self.zeroDivisor()
        elif self.type == 'unit':
            return x in self.element()
        elif self.type == 'zero divisor':
            return x in self.zeroDivisor()
        elif self.type == 'total':
            return x in self.element()
        elif self.type == 'total zero divisor':
            return x in self.zeroDivisor()
        elif self.type == 'co zero divisor':
            return x in self.coZeroDivisor()
        elif self.type == 'identitas':
            return x in self.unit()
        elif self.type == 'prima':
            return x in self.element()
        elif self.type == 'co maximal':
            return x in self.element()
        elif self.type == 'nilradical':
            return [x for x in self.element() if self.nilpotent(x) and x != 0]
        elif self.type == 'non radical':
            return [x for x in self.zeroDivisor() if not self.nilpotent(x)]
        elif self.type == 'clean':
            return x[0] in self.setOfIdempotent() and x[1] in self.unit()
        elif self.type == 'idempotent':
            return x in self.setOfIdempotent() and x != 1 and x != 0
        elif self.type == 'nilpotent':
            return not self.nilpotent(x)
        elif self.type == 'jacobson':
            return x in self.difference(self.element(),self.jacobson())
        else:
            return "kami tidak mengenali jenis graf yang anda masukkan"

    def isEdge(self, x, y):
        if x != y:
            if self.type == 'annihilator':
                return self.union(self.ann(x), self.ann(y)) != self.ann(x*y)
            elif self.type == 'unit':
                return (x+y)%self.getNumber() in self.unit()
            elif self.type == 'zero divisor':
                return x*y%self.getNumber() == 0
            elif self.type == 'total':
                return x+y%self.getNumber() in self.zeroDivisor()
            elif self.type == 'total zero divisor':
                return x*y%self.getNumber() == 0 and x+y in self.zeroDivisor()
            elif self.type == 'co zero divisor':
                return x not in [i*y for i in self.element()] and y not in [i*x for i in self.element()]
            elif self.type == 'identitas':
                return x*y%self.getNumber() == 1
            elif self.type == 'prima':
                return not any([x*i*y for i in self.element()]) or not any([y*i*x for i in self.element()])
            elif self.type == 'co maximal':
                return self.symmetriDiff([(x*i)%self.getNumber() for i in self.element()],[(i*y)%self.getNumber() for i in self.element()]) == self.element()  
            elif self.type == 'nilradical':
                return x*y%self.getNumber() == 0
            elif self.type == 'non radical':
                return x*y%self.getNumber() == 0
            elif self.type == 'clean':
                return x[0]*y[0]%self.getNumber() == 0 and x[1]*y[1]%self.getNumber() == 1
            elif self.type == 'idempotent':
                return x*y %self.getNumber() == 0
            elif self.type == 'nilpotent':
                return self.nilpotent(x+y %self.getNumber())
            elif self.type == 'jacobson':
                return (1-x*y)%self.getNumber() not in self.unit() 
            else:
                return "kami tidak mengenali graf yang anda masukkan"
             

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

    def matrixLaplacian(self):
        matrix = []
        for i in self.vertecies():
            row = []
            for j in self.vertecies():
                el = -1 if self.isEdge(i, j) else self.degree(j) if i == j else 0
                row.append(el)
            matrix.append(row)
        return matrix

    def seqDegree(self, type):
        if type == 'vertex':
            return [*map(self.degree, self.vertecies())]
        elif type == 'edge':
            return [*map(lambda y: [*map(self.degree, y)], self.edges())]
        elif type == 'not edge':
            return [*map(lambda y: [*map(self.degree, y)], self.notEdges())]
        else:
            return None