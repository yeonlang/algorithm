import sys
sys.stdin = open("벽돌깨기.txt","r")
from copy import deepcopy

def mycnt():
    cnt = 0
    for y in range(N):
        for x in range(M):
            if myMap[y][x]:
                cnt+=1
    return cnt

def arr_brick():
    for x in range(M):
        temp = []
        for y in range(N):
            if myMap[y][x]:
                temp.append(myMap[y][x])
                myMap[y][x] = 0
        for t in range(1,len(temp)+1):
            myMap[-t][x] = temp[-t]
    findtop()

def findtop():
    for i in range(M):
        top[i] == -1
    for x in range(M):
        for y in range(N-1,-1,-1):
            if y == N-1 and myMap[y][x] == 0:
                break
            if myMap[y][x]:
                top[x] = N-y
                break


def bfs(start_x):
    global myMin,flag
    cnt=mycnt()
    if cnt == 0:
        myMin = 0
        flag == False
        return
    start_y = N - top[start_x]
    stack = [(start_y, start_x, myMap[start_y][start_x])]
    myMap[start_y][start_x] = 0
    cnt -= 1
    while stack:
        y, x, t = stack.pop()
        for dx, dy in (0, 1), (0, -1), (1, 0), (-1, 0):
            time = t
            ny = y
            nx = x
            while time > 1:
                ny += dy
                nx += dx
                if 0 <= ny < N and 0 <= nx < M :
                    if myMap[ny][nx]:
                        stack.append((ny, nx, myMap[ny][nx]))
                        myMap[ny][nx] = 0
                        cnt-=1
                    time -= 1
                else:
                    break
    findtop()
    if cnt<myMin:
        myMin = cnt

def sol(tup):
    global flag
    for x in tup:
        if top[x] == -1:
            continue
        bfs(x)
        if not flag:
            return
        arr_brick()


for tc in range(int(input())):
    num,M,N = map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(N)]
    myMap = deepcopy(data)
    myMin = 987654321
    top = [-1]*M
    findtop()
    flag = True

    for a in range(M):
        if num == 1 and flag:
            sol(a)
            myMap = deepcopy(data)
            continue
        for b in range(M):
            if num == 2 and flag:
                sol((a,b))
                myMap = deepcopy(data)
                continue
            for c in range(M):
                if num == 3 and flag:
                    sol((a,b,c))
                    myMap = deepcopy(data)
                    continue
                for d in range(M):
                    if num == 4 and flag:
                        sol((a,b,c,d))
                        myMap = deepcopy(data)
                        continue
    if myMin == 987654321:
        myMin = 0
    print("#{} {}".format(tc+1,myMin))

