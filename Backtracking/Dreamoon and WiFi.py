s1 = input()
s2 = input()
expected = 0
cases = 0
valid = 0
for c in s1:
	if c == '+': expected += 1
	else: expected -= 1

def recursive(z, val):
	global expected, cases, valid
	if z == len(s2):
		if val == expected: valid += 1
		cases += 1
		return
	if s2[z] != '-': recursive(z+1, val+1)
	if s2[z] != '+': recursive(z+1, val-1)

recursive(0, 0)
print('{:.10f}'.format(1.0 * valid / cases))