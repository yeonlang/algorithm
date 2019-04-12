import sys
sys.stdin = open("과외맨.txt")

from collections import deque
def value(y,x):
    return y*N-y//2+(x-y%2)//2+1

def sol():
    for y in range(N-1, -1, -1):
        for x in range(M-1, -1, -1):
            if data[y][x] and visited[y][x]:
                print(len(visited[y][x]))
                print(*sorted(visited[y][x]))
                return

    # 우 하 상 좌
dy = [0,1,-1,0]
dx = [1,0,0,-1]

N = int(input())
M = N*2
data = [[0]*M for _ in range(N)]
visited = [[ [] for _ in range(M)] for _ in range(N)]

for y in range(N):
    if not y%2:
        for x in range(N):
            a,b = map(int,input().split())
            data[y][2*x] = a
            data[y][2*x+1] = b
    else:
        for x in range(N-1):
            a, b = map(int, input().split())
            data[y][2*x+1] = a
            data[y][2*x+2] = b

que = deque([(0,0)])
visited[0][0] = [1]
while que:
    y,x = que.popleft()
    for d in range(4):
        ny = y+dy[d]
        nx = x+dx[d]
        if 0<=ny<N and 0<=nx<M and data[ny][nx] and not visited[ny][nx]:
            if d == 0 and not y%2 and not x%2:
                visited[ny][nx] = visited[y][x]
                que.append((ny, nx))
            elif d == 3 and not y%2 and x%2:
                visited[ny][nx] = visited[y][x]
                que.append((ny, nx))
            elif d == 0 and y%2 and x%2:
                visited[ny][nx] = visited[y][x]
                que.append((ny, nx))
            elif d == 3 and y%2 and not x%2:
                visited[ny][nx] = visited[y][x]
                que.append((ny, nx))
            elif data[y][x] == data[ny][nx]:
                visited[ny][nx] = visited[y][x] + [value(ny,nx)]
                que.append((ny,nx))
sol()


