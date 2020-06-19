n, k = map(int, input().split())
incomes = list(map(int, input().split()))

res, min_income = 0, 100000

for t in incomes:
	res += t
	min_income = min(min_income, abs(t))

i, idx = 1, 0

while (i <= k):
	if (idx >= n or incomes[idx] >= 0):
		break
	res += incomes[idx] * -2
	idx += 1
	i += 1

if (i <= k):
	if ((i - k + 1) % 2 != 0):
		res -= min_income * 2
		
print(res)