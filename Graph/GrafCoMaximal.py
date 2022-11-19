class GrafComaximal:
    def __init__(self, ring):
        self.ring = ring
    def getNumber(self):
        return int(self.ring.split("_")[-1])
    def allElement(self):
        return [x for x in range(self.getNumber())]
    def getVertex(self):
        return self.allElement()
    def isEdge(self,x,y):
        A = self.elMultSet(x,self.allElement())
        B = self.elMultSet(y, self.allElement())
        return self.symmetriDiff(A,B) == self.allElement()
    def getEdge(self):
        edge = {(i,j) for i in self.getVertex() for j in self.getVertex() if i<j and self.isEdge(i,j)}
        return list(edge)
    def symmetriDiff(self, arr1, arr2):
        return [x for x in arr1 if x not in arr2]+[x for x in arr2 if x not in arr1]
    def elMultSet(self,a,arr):
        return list({(a*x)%self.getNumber() for x in arr})

    def run(self):
        ring = self.ring      
        print('---program start---')
        print(f'elemen dari {self.ring}\t:\n {self.allElement()}')
        print('-----------------------')
        print(f'annihilator dari elemen zero divisor')
        for i in self.allElement():
            print(f'{i}*{self.ring}\t:{self.elMultSet(i,self.allElement())}')
        print(f'sisi dari graf comaximal {self.ring}\t:\n{self.getEdge()}')

g = GrafComaximal('Z_6')
print(g.symmetriDiff(g.elMultSet(2,g.allElement()),g.elMultSet(3,g.allElement())))