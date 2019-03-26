import sys
sys.stdin = open("치킨배달.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BFS(y,x):
    que = [(y,x,0)]
    while que:
        y,x,cnt = que.pop(0)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny,nx) and data[ny][nx] == 2:
                return cnt+1
            elif ispass(ny,nx):
                que.append((ny,nx,cnt+1))

def DFS(c,idx):
    global myMin
    if c == K:
        cnt = 0
        for u in range(lh):
            y,x = house[u]
            cnt+=BFS(y,x)
        if cnt<myMin:
            myMin = cnt
        return

    for i in range(idx,ln):
        visited[i] = 1
        data[chicken[i][0]][chicken[i][1]] = 2
        DFS(c+1,i+1)
        data[chicken[i][0]][chicken[i][1]] = 0
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
            data[y][x] = 0
            chicken.append((y,x))
        elif data[y][x]:
            house.append((y,x))

myMin = 987654321
ln,lh = len(chicken), len(house)
visited = [0]*ln
DFS(0,0)
print(myMin)