import sys
sys.stdin = open("등산로조성.txt")

def DFS(c,flag,y,x):
    global myMax
    if c+1>myMax:
        myMax = c+1

    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if 0<=ny<N and 0<=nx<N:
            if data[y][x] > data[ny][nx] and not visited[ny][nx]:
                visited[ny][nx] = 1
                DFS(c+1,flag,ny,nx)
                visited[ny][nx] = 0
            elif data[y][x]> data[ny][nx]-K and not visited[ny][nx] and flag:
                visited[ny][nx] = 1
                temp = data[ny][nx]
                data[ny][nx] = data[y][x]-1
                DFS(c+1,False,ny,nx)
                data[ny][nx] = temp
                visited[ny][nx] = 0

dy = [1,-1,0,0]
dx = [0,0,1,-1]
visited = [[0]*8 for _ in range(8)]
for tc in range(int(input())):
    N,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    findmax = 0
    for y in range(N):
        for x in range(N):
            if data[y][x] > findmax:
                candidate = [(y,x)]
                findmax = data[y][x]
            elif data[y][x] == findmax:
                candidate.append((y,x))

    myMax = 0
    for y,x in candidate:
        visited[y][x] = 1
        DFS(0,True,y,x)
        visited[y][x] = 0
    print("#{} {}".format(tc+1,myMax))



