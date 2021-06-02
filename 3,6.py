def k_esimo_menor(A, B, k):
	if len(A) == 0:
		return B[k]
	elif len(B) == 0:
		return A[k]

	meio_de_A = len(A) // 2
	meio_de_B = len(B) // 2

	if meio_de_A + meio_de_B < k:
		if vt1[meio_de_A] > vt2[meio_de_B]:
			return k_esimo_menor(A, B[meio_de_B+1:], k - meio_de_B - 1)
		else:
			return k_esimo_menor(A[meio_de_A +1:], B, k - meio_de_A - 1)
	else:
		if vt1[meio_de_A] > vt2[meio_de_B]:
			return k_esimo_menor(A[:meio_de_A], B, k)
		else:
			return k_esimo_menor(A, B[:meio_de_B], k)
