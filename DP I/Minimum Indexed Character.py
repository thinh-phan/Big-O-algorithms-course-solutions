INF = 10**6
def hashChar(i):
    return ord(i) - ord('a')
   
def insertKey(minPos, ch, pos):
    index = hashChar(ch)
    if minPos[index] == -1:
        minPos[index] = pos
     
def getKey(minPos, ch):
    index = hashChar(ch)
    return minPos[index]
     
T = int(input())
for _ in range(T):
    str = input()
    patt = input()
   
    minPos = [-1] * 26
    for i in range(len(str)):
        insertKey(minPos, str[i], i)
     
    ans = '-'
    ansIndex = INF
    for ch in patt:
        minPosition = getKey(minPos, ch)
        if minPosition != -1 and minPosition < ansIndex:
            ans = ch
            ansIndex = minPosition
       
    if ans == '-':
        print('No character present')
    else:
        print(ans)