from Operator import Operator
from functools import reduce


class TopologiIndex(Operator):
    def __init__(self, graf):
        self.graf = graf
        self.degVertex = graf.seqDegree("vertex")
        self.degEdge = graf.seqDegree("edge")
        self.degNotEdge = graf.seqDegree("not edge")

    def run(self,topologi):
        if topologi == "narumi katayama":
            return self.NarumiKatayama()
        elif topologi == "first multiplicative zagreb":
            return self.firstMultipleZagreb()
        elif topologi == "second multiplicative zagreb":
            return self.secondMultipleZagreb()
        elif topologi == "second multiplicative zagreb coindex":
            return self.secondMultipleZagrebCoindex()
    def NarumiKatayama(self):
        return self.proc(self.degVertex)

    def firstMultipleZagreb(self, version=1):
        if version == 1:
            return self.NarumiKatayama()**2
        else:
            return self.proc(list(map(lambda x: reduce(lambda i, j: i+j, list(x)), self.degEdge)))

    def secondMultipleZagreb(self):
        return self.proc(self.flat(self.degEdge))

    def secondMultipleZagrebCoindex(self):
        return self.proc(self.flat(self.degNotEdge))

    def firstZagreb(self, version=1):
        if version == 1:
            return self.sum(self.degVertex)
        else:
            return self.sum(list(map(lambda x: reduce(lambda i, j: i+j, list(x)), self.degEdge)))

    def secondZagreb(self):
        return self.sum(list(map(lambda x: reduce(lambda i, j: i*j, list(x)), self.degEdge)))

    def geometricArithmetric(self):
        return self.sum(list(map(lambda x: reduce(lambda i,j: 2*(i*j)**(1/2)/(i+j), list(x)), self.degEdge)))
    
    def atomBondConnectivity(self):
        return self.sum(list(map(lambda x : reduce(lambda i,j: ((i+j-2)/i*j)**(1/2), list(x)), self.degEdge)))
    