import sys
sys.stdin = open("로봇청소기.txt")

def BTK(y,x,d):
    global cnt
    for i in range(1,5):
        nd = (d-i)
        if nd<0: nd += 4
        ny = y+dy[nd]
        nx = x+dx[nd]

        if not data[ny][nx]:
            cnt += 1
            data[ny][nx] = 2
            BTK(ny,nx,nd)
            return

    yy = y-dy[d]
    xx = x-dx[d]
    if data[yy][xx] != 1:
        BTK(yy,xx,d)

# 상좌하우
dy = [-1,0,1,0]
dx = [0,1,0,-1]

N,M = map(int,input().split())
y,x,d = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
data[y][x] = 2
cnt = 1
BTK(y,x,d)
print(cnt)
