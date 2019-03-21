import sys
sys.stdin = open("등산로조성.txt")

def ispass(y,x):
    return True if 0<=y<N and 0<=x<N else False

def BTK(y,x,flag):
    global cnt,result
    if cnt>result:
        result = cnt

    for dy,dx in (0,1),(-1,0),(0,-1),(1,0):
        ny = y+dy
        nx = x+dx
        if flag:
            if ispass(ny,nx) and not visited[ny][nx] and data[y][x]>data[ny][nx]:
                visited[ny][nx] = 1
                cnt+=1
                BTK(ny,nx,flag)
                cnt-=1
                visited[ny][nx] = 0
            elif ispass(ny,nx) and not visited[ny][nx] and data[ny][nx]-data[y][x]<K:
                temp=data[ny][nx]-data[y][x]+1
                data[ny][nx] -= temp
                visited[ny][nx] = 1
                cnt+=1
                flag=False
                BTK(ny,nx,flag)
                flag=True
                cnt-=1
                visited[ny][nx] = 0
                data[ny][nx] += temp

        else:
            if ispass(ny,nx) and not visited[ny][nx] and data[y][x] > data[ny][nx]:
                visited[ny][nx] = 1
                cnt+=1
                BTK(ny,nx,flag)
                cnt-=1
                visited[ny][nx] = 0


dy = [1,-1,0,0]
dx = [0,0,1,-1]
for tc in range(int(input())):
    N,K = map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    myMax = 0
    start = []

    for ay in range(N):
        for ax in range(N):
            if data[ay][ax] > myMax:
                start = [(ay,ax)]
                myMax = data[ay][ax]
            elif data[ay][ax] == myMax:
                start.append((ay, ax))

    result = 0
    for y,x in start:
        cnt = 1
        visited[y][x]=1
        BTK(y,x,True)
        visited[y][x]=0

    print("#{} {}".format(tc+1,result))



