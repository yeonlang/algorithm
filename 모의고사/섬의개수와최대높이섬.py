import sys
sys.stdin = open("섬의개수.txt","r")

def dfs(start_y,start_x):
    global my_max
    stack = [(start_y,start_x)]

    while stack:
        y,x = stack.pop()

        for nxt in range(4):
            ny = y + dy[nxt]
            nx = x + dx[nxt]
            if 0<=ny<n and 0<=nx<n and data[ny][nx] and not visited[ny][nx] :
                if data[ny][nx] > my_max:
                    my_max = data[ny][nx]
                stack.append((ny,nx))
                visited[ny][nx] = 1


for tc in range(int(input())):
    n = int(input())
    data = [list(map(int,input().split())) for _ in range(n)]
    visited = [ [0]*n for _ in range(n) ]
    result = 0
    my_max = 0
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    for y in range(n):
        for x in range(n):
            if data[y][x] and not visited[y][x]:
                if data[y][x] > my_max:
                    my_max = data[y][x]
                visited[y][x] = 1
                dfs(y,x)
                result += 1

    print("#{} {} {}".format(tc+1,result,my_max))

