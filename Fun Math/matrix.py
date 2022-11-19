def row(A):
    return len(A)

def column(A):
    return len(A[0])

def size(A):
    return [row(A), column(A)]

def add(A,B):
    if row(A) != column(B):
        return "can't calculate"
    else:
        for i in range(row(A)):
            