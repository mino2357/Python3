# prime number

N = 1000
count = 0

for i in range(2, N):
	for j in range(2, i):
		if i%j == 0:
			break
	else:
		print(i)
		count += 1

print("\n{0}".format(count))
