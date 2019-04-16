import sys
sys.stdin = open("연구소2.txt")

def spread(start):
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
stack = []
virus = []
for y in range(N):
    for x in range(N):
        if not data[y][x]:
            maxcnt+=1
        if data[y][x] == 2:
            stack.append((y,x))
            data[y][x] = 0

for start in stack:
    virus.append(spread(start))

print(virus)







