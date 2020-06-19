from math import ceil, log2

class tree:
  def __init__(self, value, lazy):
    self.value = value
    self.lazy = lazy

def calcInfo(a):
  h = ceil(log2(len(a)))
  size = 2 * (2 ** h) - 1
  return h, size

def build(a, t, k, l, r):
  if l == r:
    t[k].value= a[l]
    return
  m = (l + r) // 2
  build(a, t, k * 2 + 1, l, m)
  build(a, t, k * 2 + 2, m + 1, r)
  t[k].value = min(t[k * 2 + 1].value, t[k * 2 + 2].value)

def down(t, k):
  t[k * 2 + 1].lazy += t[k].lazy
  t[k * 2 + 1].value += t[k].lazy
  t[k * 2 + 2].lazy += t[k].lazy
  t[k * 2 + 2].value += t[k].lazy
  t[k].lazy = 0

def update(a, t, k, l, r, u, v, amount):
  if r < u or l > v:
    return 1000000000
  if u <= l and r <= v:
    t[k].value += amount
    t[k].lazy += amount
    return
  m = (l + r) // 2
  down(t, k)
  update(a, t, k * 2 + 1, l, m, u, v, amount)
  update(a, t, k * 2 + 2, m + 1, r, u, v, amount)
  t[k].value = min(t[k * 2 + 1].value, t[k * 2 + 2].value)

def query(a, t, k, l, r, u, v):
  if r < u or l > v:
    return 1000000000
  if u <= l and r <= v:
    return t[k].value
  down(t, k)
  m = (l + r) // 2
  ml = query(a, t, k * 2 + 1, l, m, u, v)
  mr = query(a, t, k * 2 + 2, m + 1, r, u, v)
  return min(ml, mr)

if __name__ == "__main__":
  n = int(input())
  a = list(map(int, input().split()))
  q = int(input())

  h, size = calcInfo(a)
  t = [tree(0, 0) for i in range(size)]
  build(a, t, 0, 0, n - 1)

  for i in range(q):
    s = list(map(int, input().split()))
    if len(s) == 2:
      if s[0] <= s[1]:
        print(query(a, t, 0, 0, n - 1, s[0], s[1]))
      else:
        x = query(a, t, 0, 0, n - 1, s[0], n - 1)
        y = query(a, t, 0, 0, n - 1, 0, s[1])
        print(min(x, y))
    else:
      if s[0] <= s[1]:
        update(a, t, 0, 0, n - 1, s[0], s[1], s[2])
      else:
        update(a, t, 0, 0, n - 1, s[0], n - 1, s[2])
        update(a, t, 0, 0, n - 1, 0, s[1], s[2])