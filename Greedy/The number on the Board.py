k = int(input())
n = input()
s = sum(int(x) for x in n)
n = sorted([9 - int(x) for x in n], reverse=True)
res = 0
for x in n:
	if s < k:
		res += 1
		s += x
print(res)