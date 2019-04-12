import sys
sys.stdin = open("감시.txt")

def fill(sy,sx,direct):
    s = set()
    for d in direct:
        y,x = sy,sx
        while True:
            y += dy[d]
            x += dx[d]
            if y == N or y == -1 or x == M or x == -1 or data[y][x] == 6:
                break
            if not data[y][x]:
                s.add((y,x))
    return s

def DFS(c,s):
    global myMax
    if c == len(cctv):
        if len(s)>myMax:
            myMax = len(s)
        return

    for news in cctv[c]:
        DFS(c+1,s|news)


    #우 하 좌 상
dy = [0,1,0,-1]
dx = [1,0,-1,0]
N, M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

R,D,L,U = 0,1,2,3

cnt = 0
cctv = []
for y in range(N):
    for x in range(M):
        if data[y][x] == 1:
            cctv.append([fill(y,x,[R]),fill(y,x,[D]),fill(y,x,[L]),fill(y,x,[U])])
        elif data[y][x] == 2:
            cctv.append([fill(y,x,[U,D]),fill(y,x,[R,L])])
        elif data[y][x] == 3:
            cctv.append([fill(y,x,[U,R]),fill(y,x,[R,D]),fill(y,x,[D,L]),fill(y,x,[L,U])])
        elif data[y][x] == 4:
            cctv.append([fill(y,x,[U,R,D]),fill(y,x,[R,D,L]),fill(y,x,[D,L,U]),fill(y,x,[L,U,R])])
        elif data[y][x] == 5:
            cctv.append([fill(y,x,[U,D,R,L])])
        if not data[y][x]:
            cnt+=1

myMax = 0
DFS(0,set())
print(cnt-myMax)

