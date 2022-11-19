import Algebra
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    
    def row(self):
        return len(self.matrix)
    
    def column(self):
        return len(self.matrix[0])
    
    def size(self):
        return (self.row(), self.column())

    def add(self,A):
        A = Matrix(A)
        rowA, columnA = A.size()
        if rowA == self.row() and columnA == self.column():
            res = []
            for i in range(A.row()):
                for j in range(self.row()):
                    res.append(A[i][j]+self.matrix[i][j])
            return res
        else:
            return "ukuran matriks yang anda masukkan tidak sama sehingga tidak dapat dilakukan operasi penjumlahan"
    
    def subtract(self,A):
        A = Matrix(A)
        rowA, columnA = A.size()
        if rowA == self.row() and columnA == self.column():
            res = []
            for i in range(A.row()):
                for j in range(self.row()):
                    res.append(A[i][j]+self.matrix[i][j])
            return res
        else:
            return "ukuran matriks yang anda masukkan tidak sama sehingga tidak dapat dilakukan operasi penjumlahan"
    
    def multiply(self, A):
        A = Matrix(A)
        row = self.row()
        column = A.column()

        if row == column:
            row = A.row()
            column = self.column()
            result = Algebra.zero(row, column)

            for i in range(row):
                for j in range(column):
                    for k in range(self.row()):
                        result[i][j] += A[i][k]*self.matrix[k][j]
        return result

    def transpose(self):
        