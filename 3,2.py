def maxFrobenius(a, b, c, d):
	n = {n for x in range(0, 101, a) for y in range(x, 101, b) for n in range(y, 101,
c) for z in range(n, 101, d)}
	g = {n for n in range(101)}
	print(max(g.difference(n)))

maxFrobenius(4,6,9,20)

possibleNNuggets = [False for i in range(100)]

validPacks = [20, 9, 6, 4]
howmany = [0, 0, 0, 0]

def NNuggets(n) :
	global howmany
	
	for i in range(len(validPacks)):
		curpack = validPacks[i]
		if(n - curpack) >= 0:
			retval = NNuggets(n-curpack)
			howmany[i] += 1
			if retval is True:
				return retval
			else:
				howmany[i] -= 1
		
		if n == 0:
			return True

	howmany = [0, 0, 0, 0]
	
	return False

n = 50

howmany = [0, 0, 0, 0]
print (n, ":", NNuggets(n), howmany)
