import sys
sys.stdin = open("치킨배달.txt")

def DFS(c,idx):
    global myMin

    if c == K:
        cnt = 0
        for u in range(lh):
            nowcnt = 987654321
            for v in range(ln):
                if visited[v]:
                    temp = abs(chicken[v][0]-house[u][0]) + abs(chicken[v][1]-house[u][1])
                    if temp<nowcnt:
                        nowcnt = temp
            cnt += nowcnt
            if cnt>=myMin: return
        if cnt < myMin:
            myMin = cnt
        return

    for i in range(idx,ln):
        visited[i] = 1
        DFS(c+1, i+1)
        visited[i] = 0


dy = [1,-1,0,0]
dx = [0,0,1,-1]

N,K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
chicken = []
house = []
for y in range(N):
    for x in range(N):
        if data[y][x] == 2:
            chicken.append((y,x))
        elif data[y][x] == 1:
            house.append((y,x))

myMin = 987654321
ln,lh = len(chicken), len(house)
visited = [0]*ln
DFS(0,0)
print(myMin)