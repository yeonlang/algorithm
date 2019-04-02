import sys
sys.stdin = open("드래곤커브.txt")

def curve(y,x,sy,sx):
    global nowy, nowx, value1
    ry ,rx = y,x
    while y != sy or x != sx:
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if visited[y][x]-visited[ny][nx] == 1 and data[ny][nx] == value:
                y = ny
                x = nx
                ry += dy[i+3 if i<1 else i-1]
                rx += dx[i+3 if i<1 else i-1]
                visited[ry][rx] = value1
                data[ry][rx] = value
                value1+=1
                break
    nowy,nowx = ry,rx

#우상좌하
dy = [0,-1,0,1]
dx = [1,0,-1,0]
data = [[0]*101 for _ in range(101)]
N = int(input())
value = 1
for y in range(N):
    sx, sy, d, g =map(int,input().split())
    data[sy][sx] = value
    nowy, nowx = sy+dy[d] , sx+dx[d]
    data[nowy][nowx] = value
    visited = [[0]*101 for _ in range(101)]
    visited[sy][sx] = 1
    visited[nowy][nowx]=2
    value1 = 3
    while g != 0:
        curve(nowy,nowx,sy,sx)
        g-=1
    value+=1
cnt = 0
for y in range(100):
    for x in range(100):
        if data[y][x] and data[y+1][x] and data[y][x+1] and data[y+1][x+1]:
            cnt+=1
print(cnt)