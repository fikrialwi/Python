from functools import reduce

class Operator:
    def union(self, arr1, arr2):
        return list(set(arr1+arr2))

    def intersect(self, arr1, arr2):
        return list(set([x for x in arr1 if x in arr2] and [y for y in arr2 if y in arr1]))

    def difference(self, arr1, arr2):
        return [x for x in arr1 if x not in arr2]

    def symmetriDiff(self,arr1,arr2):
        return [x for x in arr1 if x not in arr2 ] + [x for x in arr2 if x not in arr1]

    def clearDuplicate(self, arr):
        res = []
        for i in arr:
            if i not in res:
                res.append(i)
        return list(map(list, res))

    def sum(self, arr):
        return sum(arr)

    def proc(self, arr):
        return reduce(lambda x, y: x*y, arr) if len(arr) > 0 else 0

    def flat(self,arr):
        return [item for sublist in arr for item in sublist]

    def sumOfSet(self,arr1,arr2):
        for i,e in enumerate(arr1):
            arr2[i] +=e
        return arr2
