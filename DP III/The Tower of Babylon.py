from itertools import permutations

class block:
  def __init__(self,i):
    self.dimension = i
  def __lt__(self,other):
    for i in range(3):
      if self.dimension[i] > other.dimension[i]:
        return True
      elif self.dimension[i] < other.dimension[i]:
        return False
    return True
  def CanStack(self,other):
    if self.dimension[0] < other.dimension[0] and self.dimension[1] < other.dimension[1]:
      return True
    return False
  def __str__(self):
    return str(self.dimension[0])+ " "+str(self.dimension[1]) + \
    " " + str(self.dimension[2])


def getBlocks(blocks,a,b,c):
  arr = [a,b,c]
  arr.sort()
  b = list(permutations(arr))
  for i in(b):
    blocks.append(block(i))
  
def LIS(blocks):
  res = 0
  height = [0 for i in  range(len(blocks))]
  for i in range(len(blocks)):
    height[i] = blocks[i].dimension[2];
    for j in range(i):
      if blocks[i].CanStack(blocks[j]):
        height[i] = max(height[i], height[j] + blocks[i].dimension[2])
    res = max(res, height[i])
  return res

def main():
  n = 0
  Case = 1
  while True:
    blocks = []
    n = int(input())
    if n == 0:
      break
    for i in range(n):
      a,b,c = list(map(int, input().split()))
      getBlocks(blocks,a,b,c)
    blocks.sort()
    res = LIS(blocks)
    print('Case {}: maximum height = {}'.format(Case,res))
    Case += 1

if __name__ == "__main__":
  main()