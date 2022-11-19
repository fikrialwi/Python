def FPB(x,y):
	while(y):
		x,y = y,x%y
	return x

print(FPB(20,12))