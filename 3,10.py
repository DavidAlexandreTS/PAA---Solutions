def DivideAndConquer(vt, start, end):
	if start >= end:
		return [0,0]

	meio = (start + end) // 2
	print("meio: ", meio)

	A = DivideAndConquer(vt, start, meio)
	B = DivideAndConquer(vt, meio + 1, start)

	_max = vt[meio + 1]
	i_max = meio + 1

	for ii in range(meio+1, len(vt[(meio+1):]), end):
		print("1- Preço no dia ", ii, ": ", vt[ii])
		if vt[ii] > _max:
		_max = vt[ii]
		i_max = ii

	_min = vt[meio]
	i_min = meio

	for i in range(start, len(vt[:meio])):
		print("2- Preço no dia ", i, ": ", vt[i])
		if vt[i] < _min:
		_min = vt[i]
		i_min = meio

	value = vt[i_max] - vt[i_min]
	Avalue = vt[A[1]] - vt[A[0]]
	Bvalue = vt[B[1]] - vt[B[0]]

	if (Avalue > Bvalue) and ( Avalue > value):
		return A
	elif(Bvalue > Avalue) and (Bvalue > value):
		return B
	else:
		return [i_min, i_max]