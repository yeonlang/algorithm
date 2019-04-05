import sys
sys.stdin = open("핀볼.txt","r")

def turn(d,nxd):
    if d == 0 and (nxd ==1 or nxd ==2 or nxd == 5):
        return d-1 if d%2 else d+1

    if d == 1 and (nxd == 3 or nxd == 4 or nxd == 5):
        return d-1 if d%2 else d+1

    if d == 2 and (nxd == 1 or nxd == 4 or nxd == 5):
        return d-1 if d%2 else d+1

    if d == 3 and (nxd == 2 or nxd == 3 or nxd == 5):
        return d-1 if d%2 else d+1

    if (d == 0 and nxd == 3) or (d == 1 and nxd == 2):
        return 3
    if (d == 0 and nxd == 4) or (d == 1 and nxd == 1):
        return 2
    if (d == 2 and nxd == 3) or (d == 3 and nxd == 4):
        return 1
    if (d == 2 and nxd == 2) or (d == 3 and nxd == 1):
        return 0

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def solve(y,x,sy,sx,d,cnt):
    global myMax

    while True:
        ny = y+dy[d]
        nx = x+dx[d]
        if (ny == sy and nx == sx) or (ispass(ny,nx) and data[ny][nx] == -1):
            if cnt > myMax:
                myMax = cnt
            return

        if ispass(ny,nx):
            if 0<data[ny][nx]<6:
                nd = turn(d,data[ny][nx])
                cnt+=1
                y,x,d = ny,nx,nd
                continue
            elif data[ny][nx]>=6:
                if ny == hole[data[ny][nx]][0][0] and nx == hole[data[ny][nx]][0][1]:
                    ny,nx = hole[data[ny][nx]][1][0], hole[data[ny][nx]][1][1]
                else:
                    ny,nx = hole[data[ny][nx]][0][0], hole[data[ny][nx]][0][1]
                y,x = ny,nx
                continue
            elif not data[ny][nx]:
                y,x = ny,nx
                continue
            elif data[ny][nx] == -1:
                y,x = ny,nx
                continue
        elif ny == -1 or ny == N or nx == -1 or nx == N:
            if d%2:
                nd = d-1
            else:
                nd = d+1
            cnt += 1
            y,x,d = ny,nx,nd

   # 우 좌 상 하
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]
for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    hole = [[] for _ in range(11)]
    for y in range(N):
        for x in range(N):
            if 6 <= data[y][x] <=10:
                hole[data[y][x]].append((y,x))
    myMax = 0
    for y in range(N):
        for x in range(N):
            if data[y][x] == 0:
                for d in range(4):
                    solve(y,x,y,x,d,0)

    print("#{} {}".format(tc+1,myMax))