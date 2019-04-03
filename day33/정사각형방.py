import sys
sys.stdin = open("정사각형방.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def DFS(c,y,x,sy,sx):
    global myMax,myMin
    if c==myMax:
        if data[sy][sx]<myMin:
            myMin = data[sy][sx]
    if c>myMax:
        myMax = c
        myMin = data[sy][sx]
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ispass(ny,nx) and visited[y][x] >= visited[ny][nx] and data[ny][nx] - data[y][x] == 1 :
            visited[ny][nx] = visited[y][x]+1
            DFS(c+1,ny,nx,sy,sx)

dy = [0,1,0,-1]
dx = [1,0,-1,0]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    myMax = 0
    myMin = 987654321
    visited = [[0]*N for i in range(N)]
    for y in range(N):
        for x in range(N):
            if not visited[y][x] and N**2 - data[y][x]>=myMax:
                visited[y][x] = 1
                DFS(1,y,x,y,x)

    print("#{} {} {}".format(tc+1,myMin,myMax))