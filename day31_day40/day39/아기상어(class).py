import sys
sys.stdin = open("아기상어.txt")

from collections import deque
class Shark:
    def __init__(self,y,x,big,eat):
        self.y = y
        self.x = x
        self.big = big
        self.eat = eat
        self.ans = 0

def BFS(shark):
    visited[shark.y][shark.x] = 1
    que = deque([(shark.y,shark.x)])
    flag = 40
    fish = []
    while que:
        y,x = que.popleft()
        for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
            ny = y+dy
            nx = x+dx
            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and shark.big>=data[ny][nx] and flag>=visited[y][x]+1:
                visited[ny][nx] = visited[y][x] + 1
                if 0<data[ny][nx]<shark.big:
                    flag = visited[ny][nx]
                    fish.append((ny,nx))
                que.append((ny,nx))

    min_x = 20
    min_y = 20
    while fish:
        y,x = fish.pop()
        if y<min_y:
            min_y = y
            min_x = x
        elif y==min_y and x<min_x:
            min_y = y
            min_x = x
    if min_y == 20 and min_x == 20:
        return False

    data[min_y][min_x] = 0
    shark.ans += visited[min_y][min_x]-1
    shark.y,shark.x = min_y,min_x
    shark.eat += 1
    if shark.eat == shark.big:
        shark.big += 1
        shark.eat = 0
    return True

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if data[y][x] == 9:
            data[y][x] = 0
            shark = Shark(y,x,2,0)

visited = [[0]*N for _ in range(N)]
while BFS(shark):
    for y in range(N):
        for x in range(N):
            visited[y][x] = 0
print(shark.ans)






