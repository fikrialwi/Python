# import time


# time_start = time.time()

# def orde(p,q):
#     return p-1 if p == q else q+p-2
# def size(p,q):
#     return (p-1)*(q-2)/2 if p == q else (p-1)*(q-1)


# def test(func,data_true,*data_test):
#      for i in range(len(data_true)):
#         hasil = func(data_test[0][i],data_test[1])
#         data = data_true[i]
#         cek = data == hasil
#         tanda = "V" if cek else "X"
#         print(hasil,data,cek, tanda)


# p = [2,3,5,7,11,13,17]
# q = [2,3,5,7]
# orde_3p = [3,2,6,8,12,14,18]
# orde_5p = [5,6,4,10,14,16,20]
# orde_2p = [1,3,5,7,11,13,17]
# orde_7p = [7,8,10,6,16,18,22]

# size_3p = [2,1,8,12,20,24,32]
# size_5p = [4,8,6,24,40,48,64]
# size_2p = [0,2,4,6,10,12,16]
# size_7p = [6,12,24,15,60,72,96]

# data_orde = [orde_2p,orde_3p,orde_5p,orde_7p]
# data_size = [size_2p,size_3p,size_5p,size_7p]

# print("orde")
# for i in range(len(q)):
#         print(str(q[i]),"*",data_orde[i])
#         test(orde,data_orde[i],p,q[i])
# time_stop = time.time()-time_start

# print("size")
# for i in range(len(q)):
#     print(str(q[i]),"*",data_size[i])
#     test(size,data_size[i],p,q[i])

# print(round(time_stop,5),"s")



def NK(p,q):
	return (p-1)**(q-1)*(q-1)**(p-1) if p != q else (p-2)**(q-1)

def FMZ(p,q):
	return NK(p,q)**2
def SMZ(p,q):
	return ((q-1)*(p-1))**((q-1)*(p-1)) if p != q else (p-2)**((p-1)*(p-2))
def SMZK(p,q):
	return 0 if p==q else (p-1)**((q-1)*(q-2))*(q-1)**((p-1)*(p-2))

p = [2,3,5]
q = [2,3,5,7,11]
test = []
for i in p:
	for j in q:
		# print(f"NK({i},{j}) : {NK(i,j)}")
		# print(f"FMZ({i},{j}) : {FMZ(i,j)}")
		# print(f"SMZ({i},{j}) : {SMZ(i,j)}")
		test.append(SMZK(i,j))




 

