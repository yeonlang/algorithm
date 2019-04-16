import sys
sys.stdin = open("연구소2.txt")

from collections import deque
def spread(start):
    stack = deque([start])
    visited[start[0]][start[1]] = 1
    while stack:
        y,x = stack.popleft()
        for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
            ny = y+dy
            nx = x+dx
            if 0<=ny<N and 0<=nx<N and not data[ny][nx] and (not visited[ny][nx] or visited[y][x]+1<visited[ny][nx]):
                stack.append((ny,nx))
                visited[ny][nx] = visited[y][x]+1

def DFS(c,idx):
    global visited,myMin
    if c == K:
        s = set()
        for j in sl:
            s|=virusset[j]
        if len(s) != maxcnt:
            return
        visited = [[0]*N for _ in range(N)]
        for j in sl:
            spread(virus[j])

        maxnum = 0
        for y in range(N):
            for x in range(N):
                maxnum = max(maxnum,visited[y][x])

        if maxnum-1<myMin or myMin == -1:
            myMin = maxnum-1
        return

    for i in range(idx,V):
        sl[c] = i
        DFS(c+1,i+1)

def func(start):
    s = set([start])
    stack = [start]
    while stack:
        y,x = stack.pop()
        for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
            ny = y+dy
            nx = x+dx
            if 0<=ny<N and 0<=nx<N and not data[ny][nx] and (ny,nx) not in s:
                s.add((ny,nx))
                stack.append((ny,nx))
    return s

N,K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

maxcnt = 0
virus = []
virusset = []
for y in range(N):
    for x in range(N):
        if not data[y][x]:
            maxcnt+=1
        if data[y][x] == 2:
            virus.append((y,x))
            data[y][x] = 0
            maxcnt+=1
for start in virus:
    virusset.append(func(start))
V = len(virus)
sl = [0]*K

myMin = -1
DFS(0,0)
print(myMin)





