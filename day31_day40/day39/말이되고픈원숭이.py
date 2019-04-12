import sys
sys.stdin = open("말이되고픈원숭이.txt")

from collections import deque
def issafe(y,x): return True if 0<=y<N and 0<=x<M else False
def ispass(y,x,ny,nx,c1,c2):
    if not visited[c2][ny][nx]:
        return True
    elif visited[c2][ny][nx] > visited[c1][y][x]+1:
        return True
    return False

def BFS(c,sy,sx):
    que = deque([(sy,sx)])
    while que:
        y,x = que.popleft()
        for i in range(12):
            ny = y+dy[i]
            nx = x+dx[i]
            if issafe(ny,nx) and not data[ny][nx]:
                if i>=8 and ispass(y,x,ny,nx,c,c):
                    visited[c][ny][nx] = visited[c][y][x]+1
                    que.append((ny, nx))
                elif c<K and ispass(y,x,ny,nx,c,c+1):
                    visited[c+1][ny][nx] = visited[c][y][x]+1
                    BFS(c+1,ny,nx)

dy = [2,-2,1,-1,2,-2,1,-1,1,-1,0,0]
dx = [1,1,2,2,-1,-1,-2,-2,0,0,1,-1]
K = int(input())
N,M = map(int,input().split())
visited = [[[0]*M for _ in range(N)] for _1 in range(K+1)]
data = [list(map(int,input().split())) for _ in range(N)]
visited[0][0][0] = 1
BFS(0,0,0)

t = 987654321
for i in range(K+1):
    if visited[i][-1][-1] != 0:
        t = min(t,visited[i][-1][-1])
if t == 987654321:
    print(-1)
else:
    print(t-1)

