def prime(n):
    return factorial(n-1)%n == -1%n 

def factorial(n):
    return 1 if n == 1 else n*factorial(n-1)

def prime_gauss(a,b):
    if a != 0 and b != 0:
        return prime(a*a+b*b)
    else:
        return (a+b)%4 == 3
n = 13
i = 0
for a in range(n):
    for b in range(n):
        if prime_gauss(a,b):
            print(f"prime gaussian: {a}+{b}i")
            i+=1
print(f"jumlah prime gaussian: {i} pada {n}")