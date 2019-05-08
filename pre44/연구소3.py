import sys
sys.stdin = open("연구소3.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def DFS(c,idx):
    global result
    if c == M:
        cnt = 0
        for y in range(N):
            for x in range(N):
                if data[y][x] != 1:
                    myMin = 2500
                    for num in select:
                        myMin = myMin if myMin<visited[y][x][num] or not visited[y][x][num] else visited[y][x][num]
                    if myMin == 2500 and data[y][x] != -1:
                        return
                    if cnt < myMin and data[y][x] != -1:
                        cnt = myMin

        if result>cnt or not result:
            result = cnt
        return

    for i in range(idx,k):
        select[c] = i
        DFS(c+1,i+1)


def find(idx,start):
    que = [start]
    visited[start[0]][start[1]][idx] = 1
    while que:
        y,x = que.pop(0)
        # 좌 우 하 상
        for dy,dx in (0,-1),(0,1),(1,0),(-1,0):
            ny = y + dy
            nx = x + dx
            if ispass(ny,nx) and data[ny][nx] != 1 and not visited[ny][nx][idx]:
                visited[ny][nx][idx] = visited[y][x][idx]+1
                que.append((ny,nx))

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
virus = []
startCnt = 0

k = 0
for y in range(N):
    for x in range(N):
        if data[y][x] == 0:
            startCnt += 1
        elif data[y][x] == 2:
            virus.append((y,x))
            data[y][x] = -1
            k+=1

visited = [[[0]*k for _ in range(N)] for _ in range(N)]
for idx,start in enumerate(virus):
    find(idx,start)

select = [0]*M
result = 0
if startCnt:
    DFS(0,0)
    print(result-1)
else :
    print(0)


