import matplotlib.pyplot as plt
import time

def fibo(_max):
	sequencia, i, cont = 1, 0, 1

	while cont < _max:
		sequencia = sequencia + i
		i = sequencia - i
		cont += 1
	
	return sequencia

cont = 1
_max = 40
time_max = 0

x = list()
y = list()

while cont < _max and time_max <= 60.0:
	inic = time.time()
	sequencia = fibo(cont)
	end = time.time()
	time_current = end - inic
	print(f'{cont} {time_current:.4f}')
	x.append(cont)
	y.append(time_current)
	cont += 1
	time_max += time_current


plt.plot(x, y)
plt.xlabel('Valores de n')
plt.ylabel('Tempo (s)')
plt.xticks(range(1, 40, 2))
plt.show()