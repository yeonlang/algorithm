import sys
sys.stdin = open("테트로미노.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<M else False
def BTK(r,y,x,result):
    global myMax

    if r == 4:
        if result>myMax:
            myMax = result
        return

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ispass(ny,nx) and not visited[ny][nx]:
            visited[ny][nx] = 1
            BTK(r+1,ny,nx,result+data[ny][nx])
            visited[ny][nx] = 0


def bfs(y,x,d):
    global myMax
    result = data[y][x]
    for i in range(d,d+3):
        ny = y+dy[i%4]
        nx = x+dx[i%4]
        if ispass(ny,nx):
            result += data[ny][nx]

    if result > myMax:
        myMax = result

#상우하좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]
N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

myMax = 0
for y in range(N):
    for x in range(M):
        for d in range(4):
            bfs(y,x,d)

for y in range(N):
    for x in range(M):
        visited[y][x] = 1
        BTK(1,y,x,data[y][x])
        visited[y][x] = 0

print(myMax)
