import math

def sumOfDigit(n):
    res = 0
    while n > 0:
        res += n % 10
        n //= 10
    return res

def hashFunc(n):
    return n^sumOfDigit(n)

nCollision = 0
maxHashValue = -1
minHashValueCollision = 10 ** 9
maxFrequency = -1
mp = dict()

n = int(input())
a = list(map(int, input().split()))
for num in a:
    hash_value = hashFunc(num)
    maxHashValue = max(maxHashValue, hash_value)
    if hash_value in mp:
        mp[hash_value] += 1
    else:
        mp[hash_value] = 1

for item in mp:
    nCollision += mp[item] - 1
    maxFrequency = max(maxFrequency, mp[item])

if len(mp) == n:
    print(maxHashValue, end = " ")
else:
    for item in mp:
        if mp[item] == maxFrequency:
            minHashValueCollision = min(item, minHashValueCollision)
    print(minHashValueCollision, end = " ")
print(nCollision)