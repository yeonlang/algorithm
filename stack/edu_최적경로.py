import sys
sys.stdin = open("최적경로.txt","r")

def btk(y,nowsum):
    global minsum, visited

    if y>=n:
        nowsum += weight[y+2][1]
        if nowsum<minsum:
            minsum = nowsum
        nowsum -= weight[y + 2][1]
        return

    if nowsum > minsum:
        return

    for x in range(n):
        if not visited[x]:
            nowsum += weight[y+2][x+2]
            visited[x] = 1
            btk(y+1,nowsum)
            nowsum -= weight[y+2][x+2]
            visited[x] = 0




for tc in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    weight = [[0]*(n+2) for _ in range(n+2)]
    minsum=987654321
    visited=[0]*n
    nowsum=0

    for start in range(n+2):
        for end in range(n+2):
            weight[start][end] = abs(data[2*start]-data[2*end]) + abs(data[2*start+1]-data[2*end+1])

    for i in range(n):
        nowsum+=weight[0][i+2]
        visited[i]=1
        btk(i,nowsum)
        visited[i]=0
        nowsum-=weight[0][i+2]

