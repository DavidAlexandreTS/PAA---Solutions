def pesquisa_indice(A, esquerda, direita):
	if direita < esquerda:
		return -1
	
	meio = (esquerda + direita) // 2

	if A[meio] == A.index(A[meio]):
		return A.index(A[meio])

	else:
		return pesquisa_indice(A, esquerda, meio - 1)

A = [0, 1, 2, 3, 4, 5, 6, 8, 10]
print(pesquisa_indice(A, 0, len(A) - 1))

A = [0, 1, 2, 6, 8, 10]
print(pesquisa_indice(A, 0, len(A) - 1))

A = [1, 3, 4, 5, 6, 8, 10]
print(pesquisa_indice(A, 0, len(A) - 1))
