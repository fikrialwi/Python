def joseph(n):
    print(n)
    if len(n) ==1:
        return n
    else:
        for i,e in enumerate(n):
            if i%2 != 0:
                del n[i]
        return joseph(n)


print(joseph([*range(1,4)])) 