class GraphOfRing:
    def __init__(self,ring):
        self.ring = ring
    def getNumber(self):
        return int(self.ring.split("_")[-1])
    def cleanDuplicate(self,arr):
        res = []
        [res.append(i) for i in arr if i not in res]
        return res

class GrafAnnihilator:
    def __init__(self, ring):
        self.ring = ring
        
    def getNumber(self):
       return int(self.ring.split("_")[-1])
    def clean(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res
        
    def sum(self,arr):
        res = 0
        for i in arr:
            res += i
        return res
     
    def union(self, *arrs):
        res = []
        for arr in arrs:
            for i in arr:
                res.append(i)
        return self.clean(res)
  
    def zeroDivisor(self):
        num = self.getNumber()
        res = []
        for i in range(1,num):
            for j in range(1,num):
                if i != j and (i*j)%num == 0:
                    res.append(i)
        return self.clean(res)
       
    def annihilator(self, num):
        ring = self.getNumber()
        res = []
        for i in range(ring):
             if (i*num)%ring == 0:
                 res.append(i)
        return res
    
    def vertex(self):
        return self.zeroDivisor()
    
    def isEdge(self,vertex1, vertex2):
         return self.union(self.annihilator(vertex1), self.annihilator(vertex2)) != self.annihilator((vertex1*vertex2)%self.getNumber())
    
    def edge(self):
         res = []
         for v1 in self.vertex():
             for v2 in self.vertex():
                 if v1 < v2 and self.isEdge(v1,v2):
                     res.append((v1,v2))
         return res
         
    def orde(self):
         return len(self.vertex())
    
    def size(self):
         return len(self.edge())
    
    def neighbor(self, vertex):
         res =[]
         for v in self.vertex():
             if self.isEdge(v,vertex):
                 res.append(v)
         return res
    
    def stukturGraf(self):
         res = dict()
         for v in self.vertex():
             res[v] = self.neighbor(v)
         return res
    
    def derajat(self, vertex):
        return len(self.neighbor(vertex))
    
    def derajat_ve(self, vertex):
        neighbor = self.neighbor(vertex)
        temp = [] 
        for i in neighbor:
            temp.extend(self.neighbor(i)) 
        return len(self.clean(temp))
    
    def isMatching(self,edge1,edge2):
        return edge1[0] not in edge2 and edge1[1] not in edge2
    
    def matching(self):
        res =[]
        for i in self.edge():
            for j in self.edge():
                if self.isMatching(i,j):
                   res.append([i,j]) 
        return res
    
    def jarak(self, v1, v2):
        
        graph = self.stukturGraf()
        path = []+[v1]
        
        if v1 == v2 :
            return path
        
        if not graph.has_key(v1):
            return None
        
        shortest = None
        for u in graph[v1]:
            if u not in path:
               newpath = self.jarak(u,v2)
               if newpath:
                   if not shortest or len(newpath) < len(shortest):
                       shortest = newpath
        
        return newpath
          
    def matrixAdjency(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.isEdge(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafUnit:
    def __init__(self, ring):
        self.ring = ring
    
    def getNumber(self):
        return int(self.ring.split("_")[-1])
    
    def element(self):
        res = []
        for i in range(self.getNumber()):
           res.append(i)
        return res
    
    def clean(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res
    
    def unit(self):
        res = []
        num = self.getNumber()
        for i in range(num):
            for j in range(num):
                if i*j%num == 1:
                    res.append(i)
        return self.clean(res)
    
    def vertex(self):
        return self.element()
    
    def isEdge(self,vertex1,vertex2):
        return (vertex1 + vertex2)%self.getNumber() in self.unit()
    
    def edge(self):
        res = []
        for i in self.vertex():
            for j in self.vertex():
               if self.isEdge(i,j) and i < j:
                res.append((i,j))
        return res
    
    def clean(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res        
    
    def orde(self):
         return len(self.vertex())
    
    def size(self):
         return len(self.edge())
    
    def neighbor(self, vertex):
         res =[]
         for v in self.vertex():
             if self.isEdge(v,vertex):
                 res.append(v)
         return res
    
    def stukturGraf(self):
         res = dict()
         for v in self.vertex():
             res[v] = self.neighbor(v)
         return res
    
    def derajat(self, vertex):
        return len(self.neighbor(vertex))
    
    def derajat_ve(self, vertex):
        neighbor = self.neighbor(vertex)
        temp = [] 
        for i in neighbor:
            temp.extend(self.neighbor(i)) 
        return len(self.clean(temp))
    
    def isMatching(self,edge1,edge2):
        return edge1[0] not in edge2 and edge1[1] not in edge2
    
    def matching(self):
        res =[]
        for i in self.edge():
            for j in self.edge():
                if self.isMatching(i,j):
                   res.append([i,j]) 
        return res
    
    def matrixAdjency(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.isEdge(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix      

class GrafIdentity:
    def __init__(self, ring):
        self.ring = ring
    
    def getNumber(self):
        return int(self.ring.split("_")[-1])
    
    def clean(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res
    
    def unit(self):
        res = []
        num = self.getNumber()
        for i in range(num):
            for j in range(num):
                if i*j%num == 1:
                    res.append(i)
        return self.clean(res)
    
    def vertex(self):
        return self.unit()
    
    def isEdge(self,vertex1,vertex2):
        return (vertex1*vertex2)%self.getNumber() == 1
    
    def edge(self):
        res = []
        for i in self.vertex():
            for j in self.vertex():
               if self.isEdge(i,j) and i < j:
                res.append((i,j))
        return res       
    
    def orde(self):
         return len(self.vertex())
    
    def size(self):
         return len(self.edge())
    
    def neighbor(self, vertex):
         res =[]
         for v in self.vertex():
             if self.isEdge(v,vertex):
                 res.append(v)
         return res
    
    def stukturGraf(self):
         res = dict()
         for v in self.vertex():
             res[v] = self.neighbor(v)
         return res
    
    def derajat(self, vertex):
        return len(self.neighbor(vertex))
    
    def derajat_ve(self, vertex):
        neighbor = self.neighbor(vertex)
        temp = [] 
        for i in neighbor:
            temp.extend(self.neighbor(i)) 
        return len(self.clean(temp))
    
    def isMatching(self,edge1,edge2):
        return edge1[0] not in edge2 and edge1[1] not in edge2
    
    def matching(self):
        res =[]
        for i in self.edge():
            for j in self.edge():
                if self.isMatching(i,j):
                   res.append([i,j]) 
        return res
    
    def matrixAdjency(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.isEdge(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix      

class GrafZeroDivisor:
    def __init__(self, ring):
        self.ring = ring
        
    def getNumber(self):
       return int(self.ring.split("_")[-1])
    def clean(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res
        
    def sum(self,arr):
        res = 0
        for i in arr:
            res += i
        return res
    
    def zeroDivisor(self):
        num = self.getNumber()
        res = []
        for i in range(1,num):
            for j in range(1,num):
                if i != j and (i*j)%num == 0:
                    res.append(i)
        return self.clean(res)
    
    def vertex(self):
        return self.zeroDivisor()
    
    def isEdge(self,vertex1, vertex2):
         return vertex1 * vertex2 % self.getNumber()
    
    def edge(self):
         res = []
         for v1 in self.vertex():
             for v2 in self.vertex():
                 if v1 < v2 and self.isEdge(v1,v2):
                     res.append((v1,v2))
         return res
         
    def orde(self):
         return len(self.vertex())
    
    def size(self):
         return len(self.edge())
    
    def neighbor(self, vertex):
         res =[]
         for v in self.vertex():
             if self.isEdge(v,vertex):
                 res.append(v)
         return res
    
    def stukturGraf(self):
         res = dict()
         for v in self.vertex():
             res[v] = self.neighbor(v)
         return res
    
    def derajat(self, vertex):
        return len(self.neighbor(vertex))
    
    def derajat_ve(self, vertex):
        neighbor = self.neighbor(vertex)
        temp = [] 
        for i in neighbor:
            temp.extend(self.neighbor(i)) 
        return len(self.clean(temp))
    
    def isMatching(self,edge1,edge2):
        return edge1[0] not in edge2 and edge1[1] not in edge2
    
    def matching(self):
        res =[]
        for i in self.edge():
            for j in self.edge():
                if self.isMatching(i,j):
                   res.append([i,j]) 
        return res
    
    def matrixAdjency(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.isEdge(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix

class GrafTotal:
    def __init__(self, ring):
        self.ring = ring
        
    def getNumber(self):
       return int(self.ring.split("_")[-1])
       
    def clean(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res
    
    def element(self):
        res = []
        return [res.append(i) for i in range(self.getNumber())]
    
    def zeroDivisor(self):
        num = self.getNumber()
        res = []
        for i in range(1,num):
            for j in range(1,num):
                if i != j and (i*j)%num == 0:
                    res.append(i)
        return self.clean(res)    
    
    def vertex(self):
        return self.element()
    
    def isEdge(self,vertex1, vertex2):
         return vertex1 + vertex2 in self.zeroDivisor()
    
    def edge(self):
         res = []
         for v1 in self.vertex():
             for v2 in self.vertex():
                 if v1 < v2 and self.isEdge(v1,v2):
                     res.append((v1,v2))
         return res
         
    def orde(self):
         return len(self.vertex())
    
    def size(self):
         return len(self.edge())
    
    def neighbor(self, vertex):
         res =[]
         for v in self.vertex():
             if self.isEdge(v,vertex):
                 res.append(v)
         return res
    
    def stukturGraf(self):
         res = dict()
         for v in self.vertex():
             res[v] = self.neighbor(v)
         return res
    
    def derajat(self, vertex):
        return len(self.neighbor(vertex))
    
    def derajat_ve(self, vertex):
        neighbor = self.neighbor(vertex)
        temp = [] 
        for i in neighbor:
            temp.extend(self.neighbor(i)) 
        return len(self.clean(temp))
    
    def isMatching(self,edge1,edge2):
        return edge1[0] not in edge2 and edge1[1] not in edge2
    
    def matching(self):
        res =[]
        for i in self.edge():
            for j in self.edge():
                if self.isMatching(i,j):
                   res.append([i,j]) 
        return res
    
    def matrixAdjency(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.isEdge(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix 

class GrafTotalZeroDivisor:
    def __init__(self, ring):
        self.ring = ring
        
    def getNumber(self):
       return int(self.ring.split("_")[-1])
       
    def clean(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return res
    
    def element(self):
        res = []
        return [res.append(i) for i in range(self.getNumber())]
    
    def zeroDivisor(self):
        num = self.getNumber()
        res = []
        for i in range(1,num):
            for j in range(1,num):
                if i != j and (i*j)%num == 0:
                    res.append(i)
        return self.clean(res)    
    
    def vertex(self):
        return self.zeroDivisor()
    
    def isEdge(self,vertex1, vertex2):
         return vertex1 + vertex2 % self.getNumber() in self.zeroDivisor() and vertex1*vertex2 % self.getNumber() == 0
    
    def edge(self):
         res = []
         for v1 in self.vertex():
             for v2 in self.vertex():
                 if v1 < v2 and self.isEdge(v1,v2):
                     res.append((v1,v2))
         return res
         
    def orde(self):
         return len(self.vertex())
    
    def size(self):
         return len(self.edge())
    
    def neighbor(self, vertex):
         res =[]
         for v in self.vertex():
             if self.isEdge(v,vertex):
                 res.append(v)
         return res
    
    def stukturGraf(self):
         res = dict()
         for v in self.vertex():
             res[v] = self.neighbor(v)
         return res
    
    def derajat(self, vertex):
        return len(self.neighbor(vertex))
    
    def derajat_ve(self, vertex):
        neighbor = self.neighbor(vertex)
        temp = [] 
        for i in neighbor:
            temp.extend(self.neighbor(i)) 
        return len(self.clean(temp))
    
    def isMatching(self,edge1,edge2):
        return edge1[0] not in edge2 and edge1[1] not in edge2
    
    def matching(self):
        res =[]
        for i in self.edge():
            for j in self.edge():
                if self.isMatching(i,j):
                   res.append([i,j]) 
        return res
    
    def matrixAdjency(self):
        matrix = []
        for i in self.vertex():
            row = []
            for j in self.vertex():
                if self.isEdge(i,j):
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix 

#debugging
# graf = GrafUnit("Z_15")
# print(graf.vertex())
# print(graf.edge())
