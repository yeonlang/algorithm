import sys
sys.stdin = open("빙산.txt")

def DFS(start):
    visited = [[0]*M for _ in range(N)]
    visited[start[0]][start[1]] = 1
    stack = [start]
    cnt = 1
    while stack:
        y,x = stack.pop()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if data[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                stack.append((ny,nx))
                cnt+=1
    if cnt < len(que):
        return True

def search(y,x):
    cnt = 0
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if data[ny][nx] == 0:
            cnt+=1
    if cnt >= data[y][x]:
        data[y][x] = -1
        clean.append((y,x))
        return True
    elif data[y][x]:
        data[y][x]-=cnt

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

clean = []
dy = [1,-1,0,0]
dx = [0,0,1,-1]
que = []
for y in range(N):
    for x in range(M):
        if data[y][x]:
            que.append((y,x))

t = 1
while True:
    # que를 탐색하면서 빙하를 녹이는 부분
    i = 0
    while i != len(que):
        y,x = que[i]
        if search(y,x):
            del que[i]
            continue
        i+=1

    # -1을 0 으로 바꾸는 부분
    while clean:
        y,x = clean.pop()
        data[y][x] = 0

    # 만약 남은 빙하가 없다면 0
    if not que:
        print(0)
        break

    # 빙하가 몇조각인지 탐색
    if DFS(que[0]):
        print(t)
        break
    t+=1




