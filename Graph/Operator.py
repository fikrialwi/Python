from functools import reduce
from Algebra import Algebra


class Operator(Algebra):
    def union(self, arr1, arr2):
        return list(set(arr1+arr2))

    def intersect(self, arr1, arr2):
        return list(set([x for x in arr1 if x in arr2] and [y for y in arr2 if y in arr1]))

    def difference(self, arr1, arr2):
        return [x for x in arr1 if x not in arr2]

    def clearDuplicate(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return list(map(list, res))

    def sum(self, arr):
        return sum(arr)

    def proc(self, arr):
        return reduce(lambda x, y: x*y, arr)

    def flat(self,arr):
        return [item for sublist in arr for item in sublist]
