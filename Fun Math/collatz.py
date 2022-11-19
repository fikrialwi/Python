import matplotlib.pyplot as m
import numpy as np
def collatz(n):
    res = []
    while True:
        res.append(n)
        if n%2==0:
            n = int(n/2)
        else:
            n = 3*n+1
        if n in res:
            break
    return res
n = -51
y = collatz(n)
x = np.arange(0,len(y),1)

m.plot(x,y,'r')
m.scatter(x,y)
m.show()