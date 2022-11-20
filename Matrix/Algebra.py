class Algebra:
    def __init__(self) -> None:
        pass
    def identity(self,m):
        res = []
        for i in range(m):
            temp = []
            for j in range(m):
                temp.append(1) if i == j else temp.append(0)
            res.append(temp)
        return res

    def zero(self,m,n):
        res = []
        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(0)
            res.append(temp)
        return res