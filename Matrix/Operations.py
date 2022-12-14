import Algebra
import Matrix
class Operation(Algebra):
    def add(self, A, B):
        A = Matrix(A)
        B = Matrix(B)
        rowA, columnA = A.size()
        rowB, columnB = B.size()

        if rowA == rowB and columnA == columnB:
            res = []
            for i,x in enumerate(A):
                for j,y in enumerate(B):
                    res.append(A[i][j]+B[i][j])
            return res
        else:
            return "ukuran matriks yang anda masukkan tidak sama sehingga tidak dapat dilakukan operasi penjumlahan"
    def subtrac(self, A, B):
        A = Matrix(A)
        B = Matrix(B)
        rowA, columnA = A.size()
        rowB, columnB = B.size()

        if rowA == rowB and columnA == columnB:
            res = []
            for i,x in enumerate(A):
                for j,y in enumerate(B):
                    res.append(A[i][j]-B[i][j])
            return res
        else:
            return "ukuran matriks yang anda masukkan tidak sama sehingga tidak dapat dilakukan operasi pengurangan"
    def multiple(self, A, B):
        A = Matrix(A)
        B = Matrix(B)
        row = B.row()
        column = A.column()

        if row == column:
            row = A.row()
            column = B.column()
            result = Algebra.zero(row, column)

            for i in range(row):
                for j in range(column):
                    for k in range(B.row()):
                        result[i][j] += A[i][k]*B[k][j]
        return result
    
    def transpose(self, A):
        A = Matrix(A)
        
        row = A.row()
        column = A.column()

        result = Algebra.zero(column, row)

        for i in range(row):
            for j in range(column):
                result[j][i] == A[i][j]
        return result

    def copy(self,A):
        A = Matrix(A)
        res = self.zero(A.row(), A.column())
        for i in range(A.row()):
            for j in range(A.column()):
                res[i][j] = A[i][j]
        return res