s, b, k = input(), input(), int(input())

BASE = 29

good_strings = set()

for i in range(len(s)):
    hash = bad = 0
    for j in range(i, -1, -1):
        hash = hash * BASE + ord(s[j]) - ord('a') + 1
        if b[ord(s[j]) - ord('a')] == '0':
            bad += 1

        if bad <= k:
            good_strings.add(hash)
        else:
            break

print(len(good_strings))