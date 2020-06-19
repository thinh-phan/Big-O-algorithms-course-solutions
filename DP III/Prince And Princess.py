import bisect

def LIS(a):
  sub = [a[0]]
  
  for x in a:
    if x < sub[0]:
      sub[0] = x
    elif x > sub[-1]:
      sub.append(x)
    else:
      pos = bisect.bisect_left(sub, x)
      sub[pos] = x

  return len(sub)

def solve():
  n, p, q = map(int, input().split())
  x = list(map(int, input().split()))
  y = list(map(int, input().split()))

  pos = [-1 for i in range(n * n + 1)]
  a = []

  for i in range(len(x)):
    pos[x[i]] = i

  for i in range(len(y)):
    if pos[y[i]] >= 0:
      a.append(pos[y[i]])

  print(LIS(a))

if __name__ == "__main__":
  t = int(input())
  for i in range(t):
    print("Case ", i + 1, ": ", sep = "", end = "")
    solve()