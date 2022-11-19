from Operator import Operator

class Algebra(Operator):
    def __init__(self, ring):
        self.ring = ring

    def getNumber(self):
        return int(self.ring.split("_")[-1])

    def zeroDivisor(self):
        return list(set(x for x in range(1, self.getNumber())
                        for j in range(1, self.getNumber()) if x*j % self.getNumber() == 0))

    def unit(self):
        return list(set(x for x in range(self.getNumber()) for j in range(self.getNumber()) if x*j % self.getNumber() == 1))

    def element(self):
        return list(set(x for x in range(self.getNumber())))

    def ann(self, x):
        return list(set(r for r in range(self.getNumber()) if x*r % self.getNumber() == 0))
    
    def coZeroDivisor(self):
        return list(set(x for x in range(self.getNumber()) if x not in self.unit() and x != 0))
    
    def nilpotent(self,v):
        res = []
        i = 2
        m = v
        while m != 0:
            res.append(m)
            m = (v**i)%self.getNumber()
            if m in res:
                break
            if m == 0:
                return True
            i += 1
        return False
    
    def idempotent(self,v):
        return v**2%self.getNumber() == v
    
    def setOfIdempotent(self):
        return [x for x in self.element() if self.idempotent(x)]

    def setOfNilpotent(self):
        return [x for x in self.element() if self.nilpotent(x)]
    
    def generator(self,v):
        # gen = []
        # for i in range(self.getNumber()):
        #     gen.append(v*i%self.getNumber())
        # return gen
        res = [0]
        i = 2
        m = v
        
        while True:
            if m == 0:
                break
            res.append(m)
            m = (v*i)%self.getNumber()
            if m in res:
                break
            i += 1
        return res
    
    def idealMax(self):
        set = []
        for i in self.element():
            if self.generator(i) != self.element():
                if self.generator(i) != [1]:
                    set.append(self.generator(i))
        return self.clearDuplicate(set)
    
    def jacobson(self):
        if len(self.idealMax()) == 0:
            return []
        if len(self.idealMax()) == 1:
            return [*self.idealMax()]
        irisan = self.intersect(self.idealMax()[0], self.idealMax()[1])
        for i in self.idealMax():
            temp = self.intersect(irisan, i)
            if len(temp) < len(irisan):
                irisan = [*temp]
        return irisan
    