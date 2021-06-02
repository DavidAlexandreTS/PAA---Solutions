# Torre de Hanói 4 torres
def hanoi(n, origem, aux_1, aux_2, destino):
	if (n == 0):
		return 0

	if (n == 1):
		print("Movendo o disco", n, "de", origem, "para", destino)
		return 0

	hanoi(n - 2, origem, aux_2, destino, aux_1)

	print("Movendo o disco", n-1, "de", origem, "para", aux_2)
	print("Movendo o disco", n, "de", origem, "para", destino)
	print("Movendo o disco", n-1, "de", aux_2, "para", destino)

	hanoi(n - 2, aux_1, aux_2, origem, destino)

	n = 3
	hanoi(n, 'A', 'B', 'C', 'D')