import sys
sys.stdin = open("로봇청소기.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<M else False
def BTK(y,x,d):
    global cnt
    for i in range(1,5):
        nd = (d-i)
        if nd<0: nd += 4
        ny = y+dy[nd]
        nx = x+dx[nd]

        if ispass(ny,nx) and not data[ny][nx] and not visited[ny][nx]:
            cnt += 1
            visited[ny][nx] = 1
            BTK(ny,nx,nd)
            return

    yy = y-dy[d]
    xx = x-dx[d]
    if ispass(yy,xx) and not data[yy][xx]:
        BTK(yy,xx,d)

# 상좌하우
dy = [-1,0,1,0]
dx = [0,1,0,-1]

N,M = map(int,input().split())
y,x,d = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
visited[y][x] = 1
cnt = 1
BTK(y,x,d)
print(cnt)
