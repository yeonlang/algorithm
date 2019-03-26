import sys
sys.stdin = open("인구이동.txt")
from collections import deque

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BFS(start_y,start_x,visited):
    global flag
    que = deque([(start_y,start_x)])
    rollback = deque([(start_y,start_x)])
    nowsum = data[start_y][start_x]
    cnt = 1
    visited[start_y][start_x] = 1
    while que:
        y,x = que.popleft()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny,nx) and pmin<=abs(data[y][x] - data[ny][nx])<=pmax and not visited[ny][nx]:
                flag = True
                que.append((ny,nx))
                rollback.append((ny,nx))
                visited[ny][nx] = 1
                nowsum+=data[ny][nx]
                cnt+=1

    nowsum = nowsum//cnt
    while rollback:
        y,x = rollback.pop()
        data[y][x] = nowsum

def sol():
    global flag
    t = 0
    while True:
        flag = False
        visited = [[0] * N for _ in range(N)]
        for y in range(N):
            for x in range(N):
                if not visited[y][x]:
                    BFS(y,x,visited)
        if not flag: return t
        t+=1

dy = [-1,0,1,0]
dx = [0,1,0,-1]
N, pmin, pmax = map(int,input().split())
data = [ list(map(int,input().split())) for _ in range(N) ]
print(sol())







