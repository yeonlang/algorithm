import sys
sys.stdin = open("보급로.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BTK(y,x,cnt):
    global myMin
    if y == N-1 and x == N-1:
        if cnt<myMin:
            myMin = cnt
        return
    if cnt>=myMin:return
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ispass(ny,nx) and visited[ny][nx] == -1 :
            visited[ny][nx] = cnt+data[ny][nx]
            BTK(ny,nx,cnt+data[ny][nx])
        elif ispass(ny,nx) and cnt+data[ny][nx]<visited[ny][nx]:
            visited[ny][nx] = cnt + data[ny][nx]
            BTK(ny, nx, cnt + data[ny][nx])

dy = [1,0,-1,0]
dx = [0,1,0,-1]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input())) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]
    myMin = 987654321

    visited[0][0] = 0
    BTK(0,0,0)
    print("#{} {}".format(tc+1,myMin))

    # 1 2
    # 2 2
    # 3 8
    # 4 57
    # 5 151
    # 6 257
    # 7 18
    # 8 160
    # 9 414
    # 10 395
