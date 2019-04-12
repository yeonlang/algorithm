import sys
sys.stdin = open("벽돌깨기.txt")

def array(data):
    for x in range(M):
        temp = []
        for y in range(N):
            if data[y][x]:
                temp.append(data[y][x])
                data[y][x] = 0

        for y in range(N-1,-1,-1):
            if temp:
                data[y][x] = temp.pop()
            else:
                break

def clear(sy,sx,data):
    stack = [(sy,sx,data[sy][sx]-1)]
    data[sy][sx] = 0
    while stack:
        y,x,p = stack.pop()
        for i in range(4):
            ny,nx = y,x
            for j in range(p):
                ny+=dy[i]
                nx+=dx[i]
                if 0<=ny<N and 0<=nx<M:
                    if data[ny][nx] == 1:
                        data[ny][nx] = 0
                    elif data[ny][nx]:
                        stack.append((ny,nx,data[ny][nx]-1))
                        data[ny][nx] = 0
def DFS(c,data):
    global myMin
    if c == K:
        cnt = 0
        for y in range(N):
            for x in range(M):
                if data[y][x]:
                    cnt+=1
        myMin = min(myMin,cnt)
        return
    if data[N-1].count(0) == M:
        myMin = 0
        return
    for x in range(M):
        if data[N-1][x] == 0:
            continue
        tpdata = [da[:] for da in data]
        for y in range(N):
            if tpdata[y][x]:
                clear(y,x,tpdata)
                array(tpdata)
                break
        DFS(c+1,tpdata)

dy = [1,-1,0,0]
dx = [0,0,1,-1]
for tc in range(int(input())):
    K,M,N = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    myMin = 200
    DFS(0,data)
    print("#{} {}".format(tc+1,myMin))
