import sys
sys.stdin = open("버스.txt","r")

def dfs(start_y,start_x, start_ry, start_rx, start_d):
    global result
    stack = [(start_y,start_x,start_ry,start_rx,start_d)]

    while stack:
        y,x,ry,rx,d = stack.pop()

        if y == N-1 and x == N-1 and not (ry == y-1 and rx == x-1):
            result += 1

        for i in range(len(dx[d])):
            ny = y+dy[d][i]
            nx = x+dx[d][i]

            # 아래쪽으로 가는 거라면
            if ny == y+1 and nx == x :
                if 0<=nx<N and 0<=ny<N and not data[ny][nx]:
                    stack.append((ny, nx,y,x, 0))

            # 오른쪽으로 가는 거라면
            if ny == y and nx == x+1:
                if 0 <= nx < N and 0 <= ny < N and not data[ny][nx]:
                    stack.append((ny, nx,y,x, 1))

            # 대각선으로 가는 것이라면
            if ny == y+1 and nx == x+1:
                if 0<=nx<N and 0<=ny<N and not data[y+1][x] and not data[y][x+1]:
                    if ny+1<N and not data[ny+1][nx]:
                        stack.append((ny+1,nx,ny,nx,0))
                    if nx+1<N and not data[ny][nx+1]:
                        stack.append((ny,nx+1,ny,nx,1))
                    if nx+1<N and ny+1<N and not data[ny+1][nx+1] and not data[ny][nx+1] and not data[ny+1][nx]:
                        stack.append((ny+1,nx+1,ny,nx,2))


for tc in range(int(input())):
    N = int(input())
    data = [ list(map(int,input().split())) for _ in range(N) ]
    result = 0

    dy = [[1,1],[0,1],[1,0,1]]
    dx = [[0,1],[1,1],[0,1,1]]

    # 0 = 아래로
    # 1 = 오른쪽으로
    # 2 = 대각선으로
    if not data[0][1]:
        dfs(0,1,0,0,1)
    if not data[1][0]:
        dfs(1,0,0,0,0)
    print(result)


