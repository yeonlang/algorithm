import sys
sys.stdin = open("뱀.txt")

from collections import deque
N = int(input())
K = int(input())
data = [[0]*N for _ in range(N)]
for i in range(K):
    y,x = map(int,input().split())
    data[y-1][x-1] = 1


Direct = [0]*10001
L = int(input())
for j in range(L):
    X,C = input().split()
    Direct[int(X)] = C

    #우 하 좌 상
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
visited = deque()
hy,hx = 0,0
ty,tx = 0,0
d = 0
time = 1
data[0][0] = 2
while True:
    hy+=dy[d]
    hx+=dx[d]
    visited.append((hy,hx))

    if hy>= N or hy<0 or hx>=N or hx<0:
        break
    if data[hy][hx] == 2:
        break

    if not data[hy][hx]:
        data[ty][tx] = 0
        ty,tx = visited.popleft()

    data[hy][hx] = 2

    if Direct[time]:
        if Direct[time] == 'D':
            d = d+1 if d != 3 else 0
        elif Direct[time] == 'L':
            d = d-1 if d != 0 else 3
    time+=1
print(time)





