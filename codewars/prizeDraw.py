def prizeDraw(st,w,n):
    fArray = st.split(',')
    numArray = []
    resArray = []
    pointArr = []
    lengthName = list(map(len, fArray))
    for i in fArray:
        cr = 0
        for j in i:
            c = ord(j.upper())-64
            cr += c
        numArray.append(cr)
    
    for j in range(len(fArray)):
        resArray.append(numArray[j]+lengthName[j])
    
    
    for i,e in enumerate(resArray):
        pointArr.append(e*w[i])
    
    result = {
        name,
        point
    }
    for i,e in enumerate(fArray):
        result.add()
    

name = 'COLIN,AMANDBA,AMANDAB,CAROL,PauL,JOSEPH'
weight = [1, 4, 4, 5, 2, 1]
print(prizeDraw(name, weight, 4))

