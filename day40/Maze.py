import sys
sys.stdin = open("Maze.txt")

from collections import deque
def ispass(z,y,x): return True if 0<=z<5 and 0<=y<5 and 0<=x<5 else False
def clear():
    for x in range(5):
        for y in range(5):
            for z in range(5):
                visited[z][y][x] = 0

def BFS(data):
    global myMin
    que = deque([(0,0,0)])
    visited[0][0][0] = 1
    while que:
        z,y,x = que.popleft()
        if z == 4 and y == 4 and x == 4:
            if visited[4][4][4]-1 < myMin or myMin == -1:
                myMin = visited[4][4][4]-1
                clear()
            return
        for i in range(6):
            nz = z+dz[i]
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(nz,ny,nx) and not visited[nz][ny][nx] and data[nz][ny][nx]:
                visited[nz][ny][nx] = visited[z][y][x]+1
                que.append((nz,ny,nx))
    clear()

# 돌린 판을 고르는 중복순열
def DFS(c,tpdata):
    if c == 5:
        BFS(tpdata)
        return
    for i in range(4):
        tpdata[c] = data[result[c]][i]
        if not tpdata[0][0][0] or (c==4 and not tpdata[4][4][4]):
            continue
        DFS(c+1,tpdata)

# 판을 쌓는 순열
def permu1(c):
    if c == 5:
        DFS(0,[0,0,0,0,0])
        return

    for i in range(5):
        if not used[i]:
            result[c] = i
            used[i] = 1
            permu1(c+1)
            used[i] = 0

def turn(data):
    copy = [[0]*5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            copy[y][x] = data[4-x][y]
    return copy

visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
dz = [1,-1,0,0,0,0]
dy = [0,0,0,1,0,-1]
dx = [0,0,1,0,-1,0]

data1 = [list(map(int,input().split())) for _ in range(5)]
data2 = [list(map(int,input().split())) for _ in range(5)]
data3 = [list(map(int,input().split())) for _ in range(5)]
data4 = [list(map(int,input().split())) for _ in range(5)]
data5 = [list(map(int,input().split())) for _ in range(5)]

data = []
for t in data1,data2,data3,data4,data5:
    temp = [t]
    for i in range(3):
        t = turn(t)
        temp.append(t)
    data.append(temp)

myMin = -1
used = [0]*5
result = [0]*5
permu1(0)
print(myMin)


# 순열


