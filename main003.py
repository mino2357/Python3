#print

name = "mino2357"
score = 100.001

print("name: %s, score: %f" % (name, score))
print("name: %-10s, score: %10.10f" % (name, score))
print("name: %10s, score: %10.10f" % (name, score))

print("name:{0}, score:{1}".format(name, score))
print("name:{0:>10s}, score:{1:<10.10f}".format(name, score))
