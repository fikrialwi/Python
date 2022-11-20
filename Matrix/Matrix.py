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

    def scalar(self, c):
        res = []
        for i in range(self.row()):
            temp = []
            for j in range(self.column()):
                temp.append(c*self.matrix[i][j])
            res.append(temp)
        return res
                
    def transpose(self):
        row = self.row()
        column = self.column()

        result = Algebra.zero(column, row)

        for i in range(row):
            for j in range(column):
                result[j][i] == self.matrix[i][j]
        return result

    def determinant(self):
        if self.column() != self.row():
            return "hanya matriks persegi yang mempunyai determinan. matriks anda bukan matriks persegi"

        temp = [0]*self.row()  # temporary array for storing row
        total = 1
        det = 1  # initialize result
    
        # loop for traversing the diagonal elements
        for i in range(0, self.row()):
            index = i  # initialize the index
    
            # finding the index which has non zero value
            while(index < self.row() and self.matrix[index][i] == 0):
                index += 1
    
            if(index == self.row()):  # if there is non zero element
                # the determinant of matrix as zero
                continue
    
            if(index != i):
                # loop for swapping the diagonal element row and index row
                for j in range(0, self.row()):
                    self.matrix[index][j], self.matrix[i][j] = self.matrix[i][j], self.matrix[index][j]
    
                # determinant sign changes when we shift rows
                # go through determinant properties
                det = det*int(pow(-1, index-i))
    
            # storing the values of diagonal row elements
            for j in range(0, self.row()):
                temp[j] = self.matrix[i][j]
    
            # traversing every row below the diagonal element
            for j in range(i+1, self.row()):
                num1 = temp[i]     # value of diagonal element
                num2 = self.matrixt[j][i]   # value of next row element
    
                # traversing every column of row
                # and multiplying to every row
                for k in range(0, self.row()):
                    # multiplying to make the diagonal
                    # element and next row element equal
    
                    self.matrix[j][k] = (num1*self.matrix[j][k]) - (num2*temp[k])
    
                total = total * num1  # Det(kA)=kDet(A);
    
        # multiplying the diagonal elements to get determinant
        for i in range(0, self.row()):
            det = det*self.matrix[i][i]
    
        return int(det/total)  # Det(kA)/k=Det(A);