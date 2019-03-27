import sys
sys.stdin = open("치킨집.txt")

def DFS(c,idx):
    global result
    if c == K:
        myMin = []
        for i in range(lc):
            cnt = 0
            if visited[i]:
                temp = []
                for j in range(lh):
                    temp.append(abs(chicken[i][0] - house[j][0])+ abs(chicken[i][1] - house[j][1]))
                cnt+=sum(temp)
            myMin.append(cnt)
        if min(myMin) < result:
            result = min(myMin)
        return

    for i in range(idx,lc):
        if not visited[i]:
            visited[i] = 1
            DFS(c+1,i+1)
            visited[i] = 0


N,K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
result = 987654321
chicken = []
house = []
for y in range(N):
    for x in range(N):
        if data[y][x] == 2:
            chicken.append((y,x))
        elif data[y][x]:
            house.append((y,x))
lc,lh = len(chicken),len(house)
visited = [0]*lc
DFS(0,0)

print(result)




