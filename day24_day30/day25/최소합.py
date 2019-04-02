import sys
sys.stdin = open("최소합.txt")

def ispass(y,x):
    return True if 0<=y<n and 0<=x<n else False

def bfs(start):
    que=[start]

    while que:
        y,x = que.pop(0)
        for i in range(2):
            ny,nx = y+dy[i], x+dx[i]
            if ispass(ny,nx) and (not result[ny][nx] or result[y][x]+data[ny][nx] < result[ny][nx]):
                que.append((ny,nx))
                result[ny][nx] = result[y][x]+data[ny][nx]


for tc in range(int(input())):
    n = int(input())
    data = [ list(map(int,input().split())) for _ in range(n) ]
    result = [[0]*n for _ in range(n)]

    dy = [0,1]
    dx = [1,0]
    result[0][0] = data[0][0]
    bfs((0,0))
    print("#%d %d"%(tc+1,result[n-1][n-1]))