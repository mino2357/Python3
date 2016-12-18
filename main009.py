# list

scores = [1,2,5]
print(scores[0])
print(len(scores))
scores.append(100)
print(scores)

for score in scores:
	print(score)

print(scores)

scores.append(1010000000)

for i, score in enumerate(scores):
	print("{0}: {1}" .format(i, score))
