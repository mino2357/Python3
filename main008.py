# prime number

def countPrimeNumer(N):
	count = 0
	for i in range(2, N):
		for j in range(2, i):
			if i%j == 0:
				break
		else:
			count += 1
	return count

print(countPrimeNumer(10000))
