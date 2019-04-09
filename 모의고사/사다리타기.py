import sys
sys.stdin = open("사다리타기.txt")

def search(start_y,start_x):
    ry,rx = -1,-1
    y,x = start_y,start_x
    while True:
        if y == ln-1:
            if x == start_x:
                return True
            else :
                return False
        for i in range(3):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=ny<ln and 0<=nx<lm and data[ny][nx] and not (ny == ry and nx == rx):
                ry,rx = y,x
                y,x = ny,nx
                break

def ispass(y,x):
    if y != 0 and y != ln and (x-2<0 or not data[y][x-2]) and (x+2>=lm or not data[y][x+2]):
        return True
    else:
        return False

def BTK(choice, idx):
    global myMin
    if choice > 3:
        return
    if choice > myMin:
        return

    flag = True
    for start_x in range(0,lm+1,2):
        start_y = 0
        if flag: flag = search(start_y,start_x)
        else: break

    if flag:
        if choice<myMin:
            myMin = choice
        return

    for i in range(idx,ln*lm):
        y = i//lm
        x = i%lm
        if not data[y][x] and ispass(y,x):
            data[y][x] = 1
            BTK(choice+1, i+1)
            data[y][x] = 0

dy = [0,0,1]
dx = [-1,1,0]
N,M,H = map(int,input().split())
data = [ [0 if j%2 else 1 for j in range(N*2-1)] for i in range(H+2)]

ln = len(data)
lm = len(data[0])

for i in range(M):
    a,b = map(int,input().split())
    data[a][b*2-1] = 1

myMin = 987654321
BTK(0,0)
if myMin == 987654321:
    print(-1)
else :
    print(myMin)

