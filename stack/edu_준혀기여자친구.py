import sys
sys.stdin = open("준혀기.txt","r")

def dfs(start,nowsum):
    global minsum,result
    road.append(start)
    if start == find:
        if minsum > nowsum:
            minsum=nowsum
            print(road)
            print(minsum)
            # result=road[:]
        return
    if nowsum > minsum:
        return
    visited[start] = 1

    for nxt in range(1,n+1):
        if data[start][nxt] and not visited[nxt]:
            nxtsum=nowsum+plus[start][nxt]
            visited[nxt] = 1
            dfs(nxt,nxtsum)
            road.pop()
            visited[nxt] = 0

n,m = map(int, input().split())
data = [[0]*(n+1) for _ in range(n+1)]
plus = [[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
minsum=987654321
find=n
road=[]
result=0

for _ in range(1,m+1):
    start, end, value = map(int,input().split())
    data[start][end] = 1
    data[end][start] = 1
    plus[start][end] = value
    plus[end][start] = value

dfs(1,0)
print('end')
# print(result)
