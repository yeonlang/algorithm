import sys
sys.stdin = open("bj2658.txt","r")

def vertex(y,x):
    count = 0
    for i in range(8):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<10 and 0<=ny<10 and data[ny][nx] == 1:
            count+=1
    if count == 3:
        return 3
    if count == 2:
        return 2
    return False

data = [list(map(int,input()))for _ in range(10)]

dx = [1,-1,0,0,-1,1,-1,1]
dy = [0,0,1,-1,-1,1,1,-1]
result45 = []
result90 = []
result=[]

for y in range(10):
    for x in range(10):
        if data[y][x] and vertex(y,x):
            result.append((y+1,x+1))
            if vertex(y,x) == 3:
                result90.append((y+1,x+1))

            elif vertex(y,x) ==2:
                result45.append((y+1,x+1))

print(result90)
if len(result45) == 2 and len(result90) == 1:
    y1,x1=result45[0]
    y2,x2=result45[1]
    y3,x3=result90[0]
    c=abs(y1 - y2) ** 2 + abs(x1-x2) ** 2
    a=abs(y1 - y3) ** 2 + abs(x1-x3) ** 2
    b=abs(y2 - y3) ** 2 + abs(x2-x3) ** 2
    if c == (a+b) :
        for i in result:
            print(*i)
    else:
        print('0')
else:
    print('0')


