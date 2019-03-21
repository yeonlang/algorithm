import sys
sys.stdin = open("디저트카페.txt")

def BTK(y,x,start_y,start_x,nowdir):
    global ans
    for i in range(2):
        if nowdir+i>3:
            return
        ny=y+dy[nowdir+i]
        nx=x+dx[nowdir+i]
        if ny == start_y and nx == start_x:
            if len(visited)>ans:
                ans = len(visited)

        if 0<=ny<N and 0<=nx<N and not data[ny][nx] in visited:
            visited.add(data[ny][nx])
            BTK(ny,nx,start_y,start_x,nowdir+i)
            visited.remove(data[ny][nx])

dy = [1,1,-1,-1]
dx = [1,-1,-1,1]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    ans = -1

    for y in range(N-2):
        for x in range(N):
            visited = set([data[y][x]])
            BTK(y,x,y,x,0)

    print("#{} {}".format(tc+1,ans))



