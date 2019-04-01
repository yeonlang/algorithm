import sys
sys.stdin = open("주사위굴리기.txt")

def issafe(y,x) : return True if 0<=y<N and 0<=x<M else False
def trans(d):
    if d == 0:
        cube.top,cube.left,cube.bottom,cube.right = cube.left,cube.bottom,cube.right,cube.top
    elif d == 1:
        cube.top, cube.left, cube.bottom, cube.right = cube.right, cube.top, cube.left, cube.bottom
    elif d == 2:
        cube.top,cube.front,cube.bottom,cube.back = cube.front,cube.bottom,cube.back,cube.top
    elif d == 3:
        cube.top,cube.front,cube.bottom,cube.back = cube.back,cube.top,cube.front,cube.bottom

class cube:
    def __init__(self,value):
        self.value = value

cube.left = cube(0)
cube.right = cube(0)
cube.bottom = cube(0)
cube.top = cube(0)
cube.front = cube(0)
cube.back = cube(0)

N,M,y,x,K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
direct = list(map(lambda x: int(x)-1,input().split()))
    #우좌상하
dy = [0,0,-1,1]
dx = [1,-1,0,0]

for i in direct:
    ny=y+dy[i]
    nx=x+dx[i]
    if issafe(ny,nx):
        trans(i)
        y = ny
        x = nx
        if data[y][x]:
            cube.bottom.value = data[y][x]
            data[y][x] = 0
        else:
            data[y][x] = cube.bottom.value
        print(cube.top.value)



