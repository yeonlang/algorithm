import sys
sys.stdin = open("탈주범검거.txt")

from collections import deque

def issafe(y,x): return True if 0<=y<N and 0<=x<M else False
def ispass(y,x,ry,rx):
    for i in nxtdir[data[y][x]]:
        ny = y+dy[i]
        nx = x+dx[i]
        if issafe(ny,nx) and ny == ry and nx == rx: return True
def BFS(sy,sx):
    global cnt
    que = deque([(sy,sx,data[sy][sx])])
    visited[sy][sx] = 1
    cnt = 1
    while que:
        y,x,d = que.popleft()
        for i in nxtdir[d]:
            ny = y+dy[i]
            nx = x+dx[i]
            if issafe(ny,nx) and data[ny][nx] and not visited[ny][nx] and ispass(ny,nx,y,x) :
                que.append((ny,nx,data[ny][nx]))
                visited[ny][nx] = visited[y][x]+1
                if visited[ny][nx]>K: return
                cnt+=1

     #상 하 좌 우
dy = [-1, 1, 0, 0]
dx = [ 0, 0,-1, 1]
nxtdir = [0,[0,1,2,3],[0,1],[2,3],[0,3],[1,3],[1,2],[0,2]]
for tc in range(int(input())):
    N,M,sy,sx,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    BFS(sy,sx)
    print("#{} {}".format(tc+1,cnt))

