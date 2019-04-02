import sys
sys.stdin = open("동철이의일분배.txt")

def makemin(n,l=0):
    global myMax
    if l == n:
        return
    temp = 0
    for i in range(n):
        if not minvisited[i]:
            if data[l][i] >= temp:
                temp = data[l][i]
                vi = i
    myMax = myMax*temp
    minvisited[vi] = 1
    makemin(n,l+1)

def btk(level, n, nowMulti):
    global myMax
    if level == n:
        if nowMulti>myMax:
            myMax = nowMulti
        return
    if nowMulti < myMax:
        return
    for i in range(n):
        if not visited[i]:
            visited[i]=1
            nxtMulti= nowMulti*data[level][i]
            btk(level+1, n, nxtMulti)
            visited[i]=0

for tc in range(int(input())):
    n = int(input())
    data = [ list(map(int,input().split())) for _ in range(n) ]
    for i in range(n):
        for j in range(n):
            data[i][j]= data[i][j]/100

    myMax = 1
    minvisited = [0] * n
    makemin(n)
    visited=[0]*n

    for t in range(n):
        visited[t]=1
        btk(1,n,data[0][t])
        visited[t]=0

    myMax = myMax
    print('#%d %0.6f'%(tc+1,round(myMax*100,6)))