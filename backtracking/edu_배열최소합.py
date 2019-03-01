import sys
sys.stdin = open("배열최소합.txt","r")

def getsum(y,n,nowsum):
    global minsum, visitedX

    if y >= n:
        if nowsum < minsum:
            minsum = nowsum
            return
        return

    if nowsum > minsum:
        return

    for x in range(n):
        if not visitedX[x] :
            nowsum += data[y][x]
            visitedX[x] = 1
            getsum(y+1,n,nowsum)
            nowsum -= data[y][x]
            visitedX[x] = 0



for tc in range(int(input())):
    n=int(input())
    data=[]
    for i in range(n):
        data.append(list(map(int,input().split())))

    visitedX=[0]*n
    minsum = 10*n

    getsum(0,n,0)
    print(f"#{tc + 1} {minsum}")
