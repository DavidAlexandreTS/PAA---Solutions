def num_major(vetor, inicio, fim):
	if inicio == end:
		return vetor[inicio]

	meio  = (fim - inicio)//2 + inicio

	esquerda = num_major(vetor, inicio, meio)
	direita = num_major(vetor, meio + 1, fim)

	if esquerda == direita:
		return esquerda

	e_cont = 0;
	d_cont = 0;

	for i in range (inicio, fim + 1)
		if vetor[i] == esquerda:
			e_cont = e_cont + 1
		elif vetor[i] == direita:
			d_cont = d_cont + 1

	return esquerda if e_cont > d_cont else direita


vetor =  [1, 1, 2, 2, 3, 4, 5, 5, 5]

print("Numero Majoritario: ", num_major(vetor, 0, len(vetor) - 1))