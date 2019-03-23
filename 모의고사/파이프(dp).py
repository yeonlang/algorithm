import sys
sys.stdin = open("파이프.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BTK(y,x,d):
    global result
    if dp[d][y][x] != -1 : return dp[d][y][x]
    if y == N-1 and x == N-1: return 1

    dp[d][y][x] = 0

    for i in range(nowdir[d]):
        ny = y+dy[d][i]
        nx = x+dx[d][i]
        if ispass(ny,nx):
            nd = nxtdir[d][i]
            if nd == 0 and data[ny][nx] == 0:
                dp[d][y][x] += BTK(ny,nx,nd)
            elif nd == 1 and data[ny][nx] == 0:
                dp[d][y][x] += BTK(ny,nx,nd)
            elif nd == 2 and data[ny-1][nx] == 0 and data[ny][nx-1] == 0 and data[ny][nx] == 0:
                dp[d][y][x] += BTK(ny,nx,nd)

    return dp[d][y][x]

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
result = 0
dp = [[[-1]*N for _2 in range(N)] for _3 in range(3)]
nowdir = [2,2,3]
dy = [[0,1],[1,1],[0,1,1]]
dx = [[1,1],[0,1],[1,0,1]]
nxtdir = [[0,2],[1,2],[0,1,2]]

result = BTK(0,1,0)
print(result)