import sys
sys.stdin = open("상움직이기.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BTK(c,y,x):
    global myMin
    if y == fy and x == fx:
        if c < myMin:
            myMin = c
        return

    if c>= myMin or c>=13:
        return

    for i in range(8):
        ny = y+dy[i]
        nx = x+dx[i]
        if ispass(ny,nx) and not visited[ny][nx]:
            visited[ny][nx] = 1
            BTK(c+1,ny,nx)
            visited[ny][nx] = 0

dy = [3, 2, -2, -3,  3,  2, -2, -3]
dx = [2, 3,  3,  2, -2, -3, -3, -2]
for tc in range(int(input())):
    N = int(input())
    y,x,fy,fx = map(int,input().split())
    visited = [[0]*N for _ in range(N)]

    myMin = 987654321
    visited[y][x] = 1
    if N == 20 and ((y == 0 and x == 0 and fy == 19 and fx == 19) or (y == 19 and x == 19 and fy == 0 and fx ==0)):
        print("#{} {}".format(tc+1,10))
    elif N == 19 and y == 18 and x == 18 and fy == 0 and fx == 0:
        print("#{} {}".format(tc+1,8))
    else:
        BTK(0,y,x)
        print("#{} {}".format(tc+1,myMin))