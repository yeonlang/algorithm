import sys
sys.stdin = open("격자판의숫자이어붙이기.txt")

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BTK(c,y,x,visited):
    if c == 7:
        result.add(tuple(visited))
        return
    for i in range(4):
        ny = y+dy[i]
        nx = x+dx[i]
        if ispass(ny,nx):
            visited.append(data[y][x])
            BTK(c+1,ny,nx,visited)
            visited.pop()

dy = [-1,0,1,0]
dx = [0,1,0,-1]
for tc in range(int(input())):
    N = 4
    data = [list(map(int,input().split())) for _ in range(N)]

    result = set()
    for y in range(N):
        for x in range(N):
            BTK(0,y,x,[])

    print("#{} {}".format(tc+1,len(result)))

