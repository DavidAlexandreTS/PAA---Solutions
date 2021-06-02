import matplotlib.pyplot as plt
import time

def fibo(n):
	if n <= 1:
		return n
	else:
		return fibo(n - 1) + fibo(n - 2)

cont = 1
_max = 40
time_max = 0

x = list()
y = list()

while cont < _max and time_max <= 60.0:
	inic = time.time()
	seq_fib = fibo(cont)
	end = time.time()
	time_current = end - inic

	print(f'{cont} {time_current:.6f}')
	x.append(cont)
	y.append(time_current)
	cont += 1
	time_max += time_current

plt.plot(x, y)
plt.xlabel('Valores de n')
plt.ylabel('Tempo (s)')
plt.xticks(range(1, 40, 2))
plt.show()
