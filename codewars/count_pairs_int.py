def count_factor(x):
	fact=0
	for i in range(1,x):
		if x%i == 0:
			fact+=1
	return fact

def count_pairs_int(diff,n_max):
	num =0
	for i in range(2,n_max-diff):	
		if factor(i) == factor(i+diff):
			num += 1
	return num
print(count_pairs_int(6, 350))

		