import sys
sys.stdin = open("비버.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<M else False
def BFS():
    global cnt,nxtwater
    visited = [[0]*M for _ in range(N)]
    visited[start_y][start_x] = 1
    nxtme = [(start_y,start_x)]
    while True:
        me = nxtme[:]
        nxtme = []
        water = nxtwater[:]
        nxtwater=[]
        if not me: break
        while me:
            y,x = me.pop()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if ispass(ny,nx) and  data[ny][nx]<1 and not visited[ny][nx] and data[y][x] != 3:
                    visited[ny][nx] = visited[y][x]+1
                    if data[ny][nx] == -1:
                        cnt = visited[y][x]
                        return
                    data[ny][nx] = data[y][x]
                    nxtme.append((ny,nx))
        while water:
            y,x = water.pop()
            for i in range(4):
                ny = y+dy[i]
                nx = x+dx[i]
                if ispass(ny,nx) and data[ny][nx]<data[y][x] and data[ny][nx] != 1 and data[ny][nx] != -1:
                    data[ny][nx] = data[y][x]
                    nxtwater.append((ny,nx))


dy = [1,0,-1,0]
dx = [0,1,0,-1]
N, M = map(int,input().split())
data = [[0]*M for _ in range(N)]
nxtwater = []
for y in range(N):
    for x,value in enumerate(input()):
        if value == '*':
            nxtwater.append((y,x))
            data[y][x] = 3
        elif value == 'X': data[y][x] = 1
        elif value == 'D': data[y][x] = -1
        elif value == 'S':
            start_y,start_x = y,x
            data[y][x] = 2
        elif value == '.': data[y][x] = 0
cnt = 'KAKTUS'
BFS()
print(cnt)

