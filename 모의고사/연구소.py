import sys
sys.stdin = open("연구소.txt","r")

from itertools import combinations

def dfs(start_y,start_x,fill,num):
    stack=[(start_y,start_x)]
    fill.add((start_y,start_x))
    while stack:
        y,x =stack.pop()
        if len(fill)>result:
            return
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<N and 0<=nx<M and (data[ny][nx]==0 or data[ny][nx] == num) and not (ny,nx) in fill:
                stack.append((ny,nx))
                fill.add((ny,nx))

def func(fill):
    for y in range(N):
        for x in range(M):
            if len(fill)>result:
                return
            if data[y][x] == 0 and not (y, x) in fill:
                dfs(y, x, fill, 0)


N,M = map(int,input().split())
data = [ list(map(int,input().split())) for _ in range(N) ]
fill0 = set()

dx = [0,0,-1,1]
dy = [-1,1,0,0]
result = 987654321
func(fill0)
result = len(fill0)

for i,j,k in combinations(fill0,3):
    temp = set()
    yi,xi = i
    data[yi][xi] = 1
    yj, xj = j
    data[yj][xj] = 1
    yk, xk = k
    data[yk][xk] = 1
    func(temp)
    if result > len(temp):
        result = len(temp)
    if result ==0:
        break
    data[yi][xi] = 0
    data[yj][xj] = 0
    data[yk][xk] = 0
print(result)

