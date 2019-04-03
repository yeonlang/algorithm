import sys
sys.stdin = open("Maze.txt")

from itertools import permutations
from collections import deque
def ispass(z,y,x): return True if 0<=z<5 and 0<=y<5 and 0<=x<5 else False
def BFS(data):
    global myMin
    if not data[0][0][0]: return
    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    que = deque([(0,0,0)])
    visited[0][0][0] = 1
    while que:
        z,y,x = que.popleft()
        if z == 4 and y == 4 and x == 4:
            if visited[4][4][4] < myMin or myMin == -1:
                myMin = visited[4][4][4]
            return
        for i in range(6):
            nz = z+dz[i]
            ny = y+dy[i]
            nx = x+dx[i]
            if ispass(nz,ny,nx) and not visited[nz][ny][nx] and data[nz][ny][nx]:
                visited[nz][ny][nx] = visited[z][y][x]+1
                que.append((nz,ny,nx))

def func():
    for i in permutations([0,1,2,3,4],5):
        for n1 in range(4):
            for n2 in range(4):
                for n3 in range(4):
                    for n4 in range(4):
                        for n5 in range(4):
                            result.append(data[i[0]*4+n1])
                            result.append(data[i[1]*4+n2])
                            result.append(data[i[2]*4+n3])
                            result.append(data[i[3]*4+n4])
                            result.append(data[i[4]*4+n5])
                            BFS(result)
                            result.pop()
                            result.pop()
                            result.pop()
                            result.pop()
                            result.pop()
dz = [1,-1,0,0,0,0]
dy = [0,0,0,1,0,-1]
dx = [0,0,1,0,-1,0]

def turn(data):
    copy = [[0]*5 for _ in range(5)]
    for y in range(5):
        for x in range(5):
            copy[y][x] = data[4-x][y]
    return copy

data1 = [[list(map(int,input().split())) for _ in range(5)]]
data2 = [[list(map(int,input().split())) for _ in range(5)]]
data3 = [[list(map(int,input().split())) for _ in range(5)]]
data4 = [[list(map(int,input().split())) for _ in range(5)]]
data5 = [[list(map(int,input().split())) for _ in range(5)]]

for t in data1,data2,data3,data4,data5:
    i = 0
    temp = t[0]
    while i<3:
        temp = turn(temp)
        t.append(temp)
        i+=1

myMin = -1
result = []
data = data1+data2+data3+data4+data5
func()
print(myMin-1)


