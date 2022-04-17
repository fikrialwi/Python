class Algebra:
    def __init__(self, ring):
        self.ring = ring

    def getNumber(self):
        return int(self.ring.split("_")[-1])

    def zeroDivisor(self):
        return list(set(x for x in range(1, self.getNumber())
                        for j in range(1, self.getNumber()) if x*j % self.getNumber() == 0))

    def unit(self):
        return list(set(x for x in range(self.getNumber()) for j in range(self.getNumber()) if x*j % self.getNumber() == 1))

    def elememt(self):
        return list(set(x for x in range(self.getNumber())))

    def ann(self, x):
        return list(set(r for r in range(self.getNumber()) if x*r % self.getNumber() == 0))
    