class GrafAnnihilator:
    def __init__(self, ring):
        self.ring = ring
    def getNumber(self):
        return int(self.ring.split("_")[-1])
    def zeroDivisor(self):
        return list(set(x for x in range(1, self.getNumber())
                        for j in range(1, self.getNumber()) if x*j % self.getNumber() == 0))
    def ann(self, x):
        return list(set(r for r in range(self.getNumber()) if x*r % self.getNumber() == 0 and r != x))
    def getVertex(self):
        return self.zeroDivisor()
    def getEdge(self):
        edge = {(i,j) for i in self.getVertex() for j in self.getVertex() if i<j and self.union(self.ann(i), self.ann(j)) != self.ann(i*j)}
        return list(edge)
    def union(self, arr1, arr2):
        return list(set(arr1+arr2))

    def run(self):
        ring = self.ring      
        print('---program start---')
        print(f'zero divisor dari {self.ring}\t:\n {self.zeroDivisor()}')
        print('-----------------------')
        print(f'annihilator dari elemen zero divisor')
        for i in self.zeroDivisor():
            print(f'ann({i})\t:{self.ann(i)}')
        print(f'sisi dari graf annihilator {self.ring}\t:\n{self.getEdge()}')

g = GrafAnnihilator('Z_25')
g.run()