import sys
sys.stdin = open("구슬탈출.txt")

from collections import deque
def nxt(red_y,red_x,blue_y,blue_x,d):
    ry,rx,by,bx = red_y,red_x,blue_y,blue_x
        # 우 하 좌 상
    if (d == 1 and ry>by) or (d == 3 and by>ry) or (d == 2 and bx>rx) or (d==0 and rx>bx):
        while True:
            ry+=dy[d]
            rx+=dx[d]
            if 0<data[ry][rx]<4:
                ry-=dy[d]
                rx-=dx[d]
                data[ry][rx] = 2
                break
            elif data[ry][rx] == 9:
                break
        while True:
            by+=dy[d]
            bx+=dx[d]
            if 0<data[by][bx]<4 :
                by-=dy[d]
                bx-=dx[d]
                data[ry][rx] = 0
                break
            elif data[by][bx] == 9:
                if data[ry][rx] != 9:
                    data[ry][rx] = 0
                return red_y,red_x,blue_y,blue_x
    else:
        while True:
            by+=dy[d]
            bx+=dx[d]
            if 0<data[by][bx]<4:
                by-=dy[d]
                bx-=dx[d]
                data[by][bx] = 3
                break
            elif data[by][bx] == 9:
                return red_y,red_x,blue_y,blue_x
        while True:
            ry+=dy[d]
            rx+=dx[d]
            if 0<data[ry][rx]<4:
                ry-=dy[d]
                rx-=dx[d]
                data[by][bx] = 0
                break
            elif data[ry][rx] == 9:
                data[by][bx] = 0
                break

    return ry,rx,by,bx

def BFS(red_y, red_x, blue_y, blue_x):
    global myMin
    que = deque([(red_y,red_x,blue_y,blue_x)])
    visited[red_y][red_x][blue_y][blue_x] = 1
    while que:
        ry,rx,by,bx = que.popleft()
        for d in range(4):
            Ry,Rx,By,Bx = nxt(ry,rx,by,bx,d)
            if not visited[Ry][Rx][By][Bx] and visited[ry][rx][by][bx]<=10:
                if Ry == fy and Rx == fx and (By != fy or Bx != fx):
                    myMin = visited[ry][rx][by][bx]
                    return
                visited[Ry][Rx][By][Bx] = visited[ry][rx][by][bx]+1
                que.append((Ry,Rx,By,Bx))

# 우 하 좌 상
dy = [0,1,0,-1]
dx = [1,0,-1,0]

N,M = map(int,input().split())
visited =[[[[0]*M for _2 in range(N)] for _3 in range(M)] for _4 in range(N)]
data = [list(input()) for _ in range(N)]

for y in range(N):
    for x in range(M):
        if data[y][x] == '#':
            data[y][x] = 1
        elif data[y][x] == '.':
            data[y][x] = 0
        elif data[y][x] == 'R':
            red_y,red_x = y,x
            data[y][x] = 0
        elif data[y][x] == 'B':
            blue_y,blue_x = y,x
            data[y][x] = 0
        elif data[y][x] == 'O':
            fy,fx = y,x
            data[y][x] = 9

myMin = 11
BFS(red_y,red_x,blue_y,blue_x)
if myMin == 11:
    print(-1)
else:
    print(myMin)

