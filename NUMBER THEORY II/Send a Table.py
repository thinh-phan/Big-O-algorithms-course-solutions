phi_cache = [0 for _ in range(50001)]

def eulerPhi(n):
	if phi_cache[n] > 0:
		return phi_cache[n]
	
	res = n
	m = n
	for i in range(2, int(n**0.5 + 1)):
		if n % i == 0:
			while n % i == 0:
				n //= i
			res = res // i * (i - 1)

	if n > 1:
		res = res // n * (n - 1)

	phi_cache[m] = res
	return res


while True:
	n = int(input())
	if n == 0:
		break
	
	res = 1
	for y in range(2, n + 1):
		res += eulerPhi(y) * 2
	
	print(res)