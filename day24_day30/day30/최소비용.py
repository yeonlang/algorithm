import sys
sys.stdin = open("최소비용.txt")

def ispass(ny,nx,y,x):
    if 0<=ny<N and 0<=nx<N :
        if data[ny][nx]-data[y][x]>0:
            if visited[ny][nx] == -1 or visited[ny][nx] > data[ny][nx] - data[y][x] + visited[y][x] + 1:
                visited[ny][nx] = data[ny][nx] - data[y][x] + visited[y][x] + 1
                return True
        else:
            if visited[ny][nx]==-1 or visited[ny][nx]> visited[y][x]+1:
                visited[ny][nx] = visited[y][x]+1
                return True
    return False

def BFS(y,x):
    que = [(y,x)]
    visited[y][x] = 0
    while que:
        y,x = que.pop(0)
        for i in range(4):
            ny = y +dy[i]
            nx = x +dx[i]
            if ispass(ny,nx,y,x):
                que.append((ny,nx))

dy = [1,0,-1,0]
dx = [0,1,0,-1]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]

    BFS(0,0)
    print("#{} {}".format(tc+1,visited[N-1][N-1]))