def CreatHash(s):
    power[0] = 1
    for i in range(len(s)):
        hash[i + 1] = (hash[i] * BASE + ord(s[i])) % MOD
        power[i + 1] = (power[i] * BASE) % MOD

def GetHash(l, r):
    return ((hash[r] - (hash[l - 1] * power[r - l + 1]) % MOD + MOD) % MOD)

BASE = 29
MOD = int(1e9) + 7
maxn = int(5e5) + 100
cnt = [0] * 2
cntNeed = [0] * 2
power = maxn * [0]
hash = maxn * [0]
st = ''
s = input()
t = input()
n = len(s)
m = len(t)
for i in range(n):
    cnt[ord(s[i]) - ord('0')] += 1
for i in range(m):
    cnt[ord(t[i]) - ord('0')] -= 1
if cnt[0] < 0 or cnt[1] < 0:
    print(s)
    exit()
CreatHash(t)
MaxPrefixDuplicate = 0
for len in range(m - 1, -1, -1):
    if GetHash(1, len) == GetHash(m - len + 1, m):
        MaxPrefixDuplicate = len
        break 

for i in range(MaxPrefixDuplicate, m):
    cntNeed[ord(t[i]) - ord('0')] += 1
    st += t[i]

mNeed = m - MaxPrefixDuplicate
sb = t
print(MaxPrefixDuplicate, mNeed, sb , st)
while (cnt[0] >= cntNeed[0] and cnt[1] >= cntNeed[1]):
        cnt[0] -= cntNeed[0]
        cnt[1] -= cntNeed[1]
        for i in range(mNeed):
            sb += st[i]

for i in range(cnt[0]):
    sb += '0'
for i in range(cnt[1]):
    sb += '1'
print(sb)