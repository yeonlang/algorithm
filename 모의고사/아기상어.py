import sys
sys.stdin = open("아기상어.txt")

def BFS():
    global big,start_y,start_x,result,cnt
    length = 987654321
    flag = True
    fish = []
    que = [(start_y,start_x)]
    visited = [[-1] * N for _ in range(N)]
    visited[start_y][start_x] = 0

    while que:
        y,x = que.pop(0)
        if 0<data[y][x]<9 and big > data[y][x] and visited[y][x]<=length:
            fish.append((y,x))
            if flag :
                length = visited[y][x]
                flag = False

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=nx<N and 0<=ny<N and visited[ny][nx] == -1 and data[ny][nx]<=big:
                visited[ny][nx] = visited[y][x]+1
                que.append((ny,nx))

    if fish:
        fish.sort(key=lambda x: (x[0], x[1]))
        yy, xx = fish.pop(0)
        result += visited[yy][xx]
        cnt += 1
        if cnt == big:
            cnt = 0
            big += 1
        start_y, start_x = yy, xx
        data[yy][xx] = 0
        return True
    return False

dy = [-1,0,0,1]
dx = [0,-1,1,0]

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if data[y][x] == 9:
            start_y = y
            start_x = x
            data[y][x] = 0

result = 0
cnt = 0
big = 2
while BFS(): pass
print(result)
