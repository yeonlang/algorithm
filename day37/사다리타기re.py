import sys
sys.stdin = open("사다리타기.txt")

def search(start_y,start_x):
    y,x = start_y,start_x
    while True:
        if y == ln-1:
            if x == start_x:
                return True
            else :
                return False
        if x+2<lm and data[y][x+1]:
            y, x = y+1, x+2
        elif x-2>=0 and data[y][x-1]:
            y, x = y+1, x-2
        else:
            y, x = y+1, x

def BTK(c, iy, ix):
    global myMin
    if c == choice:
        for sx in range(0,lm+1,2):
            if search(0,sx):
                continue
            else:
                return
        myMin = c
        return

    for y in range(iy,ln-1):
        for x in range(ix,lm,2):
            if not data[y][x] and (x-2<0 or not data[y][x-2]) and (x+2>=lm or not data[y][x+2]):
                data[y][x] = 1
                if x == (lm-2):
                    BTK(c+1,y+1,1)
                else:
                    BTK(c+1,y,x+2)
                data[y][x] = 0
        ix = 1

dy = [0,0,1]
dx = [-1,1,0]
N,M,H = map(int,input().split())
data = [[0 if j%2 else 1 for j in range(N*2-1)] for i in range(H+2)]

ln = len(data)
lm = len(data[0])

for i in range(M):
    a,b = map(int,input().split())
    data[a][b*2-1] = 1

myMin = 4
choice = 0
while choice<4:
    BTK(0,1,1)
    if myMin == 4:
        choice+=1
    else:
        break
if myMin == 4:
    print(-1)
else :
    print(myMin)

