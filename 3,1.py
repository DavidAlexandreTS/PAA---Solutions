def virar(a, maior_panquecax):
	top = 0
	while top < maior_panquecax:
		aux = a[top]
		a[top] = a[maior_panquecax]
		a[maior_panquecax] = aux
		top = top +1
		maior_panquecax = maior_panquecax -1

def indice_maior_panqueca(a, tamanho_de_a):
	indice = 0

	for i in range(tamanho_de_a):
		if a[i] > a[indice]:
			indice = i
	return indice

def ordenar(a):
	tamanho_de_a = len(a)
	
	while tamanho_de_a > 1:
		maior_panquecax = indice_maior_panqueca(a, tamanho_de_a)
	
	print("\na: ", a, "Maior panqueca da vez: ", a[maior_panquecax],"\tIndice da maior panqueca: [", maior_panquecax, "]")

	if maior_panquecax == tamanho_de_a-1:
		tamanho_de_a = tamanho_de_a - 1
		print("Não precisa virar.")
	else:
		if tamanho_de_a != 2:
			virar(a, maior_panquecax) 
	
			print("Virou para o top", panquecas)
		
		virar(a, tamanho_de_a - 1) 
		print("Virou para a base", panquecas)
		tamanho_de_a = tamanho_de_a - 1

panquecas = [2, 4, 6, 1, 3, 7, 5]
print(panquecas)
print(len(panquecas))
ordenar(panquecas)
print("\nFinal: ", panquecas)