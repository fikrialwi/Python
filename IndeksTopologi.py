class TopologiIndicies:
    def __init__(self, graf):
        self.graf = graf
        self.verticies = graf.vertex()
        self.orde = graf.orde()
        self.edges = graf.edge()
        self.size = graf.size()
        self.derajat = graf.derajat
    
    def proc(self,arr):
        res = 1
        for i in arr:
            res *= i
        return res
    
    def sum(self,arr):
       res = 0
       for i in arr:
          res += 1
       return res
    
    def narumiKatayama(self):
        
        seqDegree = list(map(self.derajat,self.verticies))
        return self.proc(seqDegree)
        
    def firstMultipleZagreb(self):
        temp1 = self.narumiKatayama()**2
        temp2 = []
        for edge in self.edges:
            temp2.append(self.derajat(edge[0])+self.derajat(edge[1]))
        temp2 = self.proc(temp2)  
        return (temp1, temp2)
    
    def secondMultipleZagreb(self):
        res = []
        for edge in self.edges:
            for e in edge:
                res.append(self.derajat(e))
        return self.proc(res)
    
    def firstZagreb(self):
       res = []
       for edge in self.edges:
          res.append(self.derajat(edge[0])+self.derajat(edge[1]))
       res = self.sum(res)
       return res
      
    def secondZagreb(self):
        res = []
        for edge in self.edges:
          res.append(self.derajat(edge[0])*self.derajat(edge[1]))
        res = self.sum(res)
        return res
    
    