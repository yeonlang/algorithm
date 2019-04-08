import sys
sys.stdin = open("벽부수고이동하기.txt")

from collections import deque
def ispass(y,x): return True if 0<=y<N and 0<=x<M else False
def BFS(sy,sx,scan):
    global myMin
    que = deque([(sy,sx,scan)])
    while que:
        y,x,can = que.popleft()
        if y == N-1 and x == M-1:
            myMin = visited[can][y][x]
            return
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny,nx):
                if not data[ny][nx] and not visited[can][ny][nx]:
                    visited[can][ny][nx] = visited[can][y][x]+1
                    que.append((ny, nx,can))
                elif can and not visited[can-1][ny][nx]:
                    visited[can-1][ny][nx] = visited[can][y][x]+1
                    que.append((ny, nx, can-1))

dy = [1,-1,0,0]
dx = [0,0,1,-1]

N,M,K = map(int,input().split())
data = [list(map(int,input())) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(K+1)]
visited[K][0][0] = 1
myMin = -1
BFS(0,0,K)
print(myMin)