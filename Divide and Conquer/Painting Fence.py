import sys
 
 
def strokesNeeded(left, right, paintedHeight):
    if left > right:
        return 0
 
    mini = left + a[left:right+1].index(min(a[left:right+1]))
 
    allVerticle = right - left + 1
    recursive = a[mini] - paintedHeight + strokesNeeded(left, mini - 1, a[mini]) + strokesNeeded(mini + 1, right, a[mini])
 
    return min(allVerticle, recursive)
 
 
sys.setrecursionlimit(10000)
 
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
 
    print(strokesNeeded(0, n - 1, 0))