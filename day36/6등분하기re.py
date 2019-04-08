import sys
sys.stdin = open("6등분하기.txt")

def sumarea(sy,ey,sx,ex):
    cnt = 0
    for y in range(sy,ey):
        for x in range(sx,ex):
            cnt+=data[y][x]
    return cnt

def DFS(c,idx):
    global myMax
    if c == 3:
        cnt = abs(mySum[result[0]]-mySum[result[1]]) + abs(mySum[result[1]]-mySum[result[2]]) + abs(mySum[result[2]]-mySum[result[0]])
        if cnt>myMax:
            myMax = cnt
        return

    for i in range(idx,6):
        result[c] = i
        DFS(c+1,i+1)

for tc in range(int(input())):
    N,M = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    result = [0,0,0]
    myMax = 0
    for y in range(1,N):
        for x1 in range(1,M-1):
            for x2 in range(x1+1,M):
                mySum = [sumarea(0,y,0,x1),sumarea(0,y,x1,x2),sumarea(0,y,x2,M),sumarea(y,N,0,x1),sumarea(y,N,x1,x2),sumarea(y,N,x2,M)]
                DFS(0,0)
    print("#{} {}".format(tc+1,myMax))