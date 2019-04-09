import sys
sys.stdin = open("인구이동.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def DFS(sy,sx):
    global flag,result
    num = 1
    cnt = data[sy][sx]
    stack = [(sy,sx)]
    rollback = [(sy,sx)]
    visited[sy][sx] = t
    while stack:
        y,x = stack.pop()
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(ny,nx) and L<=abs(data[ny][nx]-data[y][x])<=R and visited[ny][nx]<t:
                visited[ny][nx] = t
                stack.append((ny, nx))
                rollback.append((ny,nx))
                num+=1
                cnt+=data[ny][nx]

    val = cnt//num
    for y,x in rollback:
        data[y][x] = val

    if num>1:
        result+=1
        flag = False

dy = [1,-1,0,0]
dx = [0,0,1,-1]

N,L,R = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
result = 0

t = 1
while True:
    flag = True
    for y in range(N):
        for x in range(N):
            if visited[y][x]<t:
                DFS(y,x)
    if flag:
        break
    t+=1
print(t-1)