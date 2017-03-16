x = open("1.txt")
y = open("2.txt")

x = x.readlines()[0]
y =  y.readlines()[0]
counter = 0
ret = []
while counter < len(x):
	if x[counter] != y[counter]:
		ret = [x[counter],] + ret
		#ret.append(y[counter])
	counter += 1

print ''.join(ret)
