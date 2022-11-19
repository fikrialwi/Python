class CartesianSet:
    def __init__(self,ring1,ring2):
        self.ring1 = ring1
        self.ring2 = ring2
    def elements(self):
        return [(x,y) for x in range(self.getNumber(self.ring1))for y in range(self.getNumber(self.ring2))]

    def getNumber(self,ring):
        return int(ring.split("_")[-1])

    def cross(self,x,y):
        return (x[0]*y[0]%self.getNumber(self.ring1), x[1]*y[1]%self.getNumber(self.ring2))

    def cayley_table(self):
        txt = []
        for x in self.elements():
            tx = []
            for y in self.elements():
                tx.append(self.cross(x,y))
            txt.append(tx)
        return self.print_matrix(txt)

    def print_matrix(self,m):
        st = ''
        for i,e in enumerate(m):
            for j in e:
                st += str(j)+' '
            st += '\n'
        return st

    def setZeroDivisor(self):
        zeroDivisor = set()
        for i in self.elements():
            for j in self.elements():
                if self.cross(i,j) == (0,0) and i != (0,0) and j != (0,0):
                    zeroDivisor.add(i)
        return list(zeroDivisor)

    def annihilator(self,x):
        ann = set()
        for i in self.elements():
            if self.cross(i,x) == (0,0):
                ann.add(i)
        return list(ann)

    def vertex(self):
        return self.setZeroDivisor()
    
    def isEdge(self,x,y):
        return self.annihilator(self.cross(x,y)) != list(set(self.annihilator(x)+self.annihilator(y)))

    def edge(self):
        ed = set()
        for i in self.vertex():
            for j in self.vertex():
                if i != j and self.isEdge(i,j):
                    ed.add((i,j))
        return list(ed)

    def neighboor(self,v):
        return [x for x in self.vertex() if self.isEdge(v,x)]
    
    def degree(self,v):
        return len(self.neighboor(v))

    def seqDegree(self):
        return [self.degree(x) for x in self.vertex()]

    def run(self):
        doc = open(f'property {self.ring1}X{self.ring2}.txt','w')
        txt = str(self.elements())+'\n\n'
        txt += self.cayley_table()
        txt += f'\nZ({self.ring1} x {self.ring2}) : {self.setZeroDivisor()}\n\n'
        for i in self.setZeroDivisor():
            txt += f'ann({i}) : {self.annihilator(i)}\n'

        txt += f"\nGraf Annihilator ({self.ring1}X{self.ring2})\n\n"
        
        txt += f'V\t:{self.vertex()}\n'
        txt += f"E\t:{self.edge()}"
        doc.write(txt)


C = CartesianSet('Z_3','Z_2')
C.run()
