def ponto_max(A, esquerda, direita):
	if direita < esquerda:
		return -1

	meio = (esquerda + direita) // 2

	if A[meio] > A[meio -1] and A[meio] > A[meio + 1]:
		return A[meio]
	
	elif A[meio] > A[meio -1] and A[meio] < A[meio + 1]:
		return ponto_max(A, meio, direita)

	elif A[meio] < A[meio -1] and A[meio] > A[meio + 1]:
		return ponto_max(A, esquerda, meio)

A = [ 1, 3, 5, 7, 9, 11, 13, 14, 15, 16, 18, 10, 2 ]
print(ponto_max(A, 0, len(A) - 1))

A = [ 1, 3, 5, 7, 15, 10, 8, 6, 4, 2 ]
print(ponto_max(A, 0, len(A) - 1))

A = [ 1, 6, 4, 2 ]
print(ponto_max(A, 0, len(A) - 1))