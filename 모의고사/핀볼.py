import sys
sys.stdin = open("핀볼.txt","r")

def nxtdir(d,r):
    if d == 0:
        if r in [1, 4, 5]:
            d = 1
        elif r == 2:
            d = 3
        elif r == 3:
            d = 2
    elif d == 1:
        if r in [2, 3, 5]:
            d = 0
        elif r == 1:
            d = 3
        elif r == 4:
            d = 2
    elif d == 2:
        if r in [3, 4, 5]:
            d = 3
        elif r == 1:
            d = 0
        elif r == 2:
            d = 1
    elif d == 3:
        if r in [1, 2, 5]:
            d = 2
        elif r == 3:
            d = 1
        elif r == 4:
            d = 0
    return d

def solution(start,d):
    y,x = start
    ans = 0
    while True:
        nx = x+dx[d]
        ny = y+dy[d]

        # 다음 지점이 벽일때
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
            ny = y
            nx = x
            ans += 1

        # 다음지점이 웜홀일때
        if 6 <= data[ny][nx] <= 10:
            y, x = wormhole[(ny, nx)]
            continue

        #다음지점이 블록일때
        if 1<= data[ny][nx] <=5:
            r = data[ny][nx]
            d = nxtdir(d,r)
            ans += 1
            y = ny
            x = nx
            continue

        # 다음지점이 블랙홀이거나 시작점일때
        if (ny, nx) == start or data[ny][nx] == -1:
            return ans

        y = ny
        x = nx

#상하좌우
dx=[0,0,-1,1]
dy=[-1,1,0,0]

for tc in range(int(input())):
    n = int(input())
    data = [ [0]*n for _ in range(n)]
    wormhole = {}
    tempdic = {}
    result = 0
    for now_y in range(n):
        temp=list(map(int,input().split()))
        for now_x in range(n):
            if temp[now_x] != 0:
                if 6<= temp[now_x] <=10:
                    if temp[now_x] in tempdic:
                        tempdic[temp[now_x]].append((now_y,now_x))
                    else:
                        tempdic[temp[now_x]]=[(now_y,now_x)]
                data[now_y][now_x] = temp[now_x]
    for u in tempdic.values():
        wormhole[u[0]] = u[1]
        wormhole[u[1]] = u[0]

    for y in range(n):
        for x in range(n):
            if data[y][x] == 0:
                for i in range(4):
                    temp = solution((y,x),i)
                    if temp > result:
                        result = temp

    print("#{} {}".format(tc+1,result))