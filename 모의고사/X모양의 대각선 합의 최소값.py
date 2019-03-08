import sys
sys.stdin = open("대각선.txt","r")

def up_cross(y0,x0):
    y,x = y0,x0
    temp = set()
    dy, dx = -1, 1
    for i in range(K):
        temp.add((y,x))
        y+=dy
        x+=dx
    return temp

def down_cross(y0,x0):
    y, x = y0, x0
    temp = set()
    dy, dx = 1, 1
    for i in range(K):
        temp.add((y, x))
        y += dy
        x += dx
    return temp

def sol(down,up):
    global result
    dcross=0
    ucross=0
    for y,x in down:
        dcross+=data[y][x]
    for y,x in up:
        ucross += data[y][x]
    if abs(dcross-ucross) < result:
        result = abs(dcross-ucross)

for tc in range(int(input())):
    N,K =map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(N)]

    result = 987654321
    dogu = []
    for y in range(N-K+1):
        for x in range(N-K+1):
            dogu.append((down_cross(y,x),up_cross(y+K-1,x)))

    for set1,set2 in dogu:
        sol(set1,set2)

    print("#{} {}".format(tc+1,result))


