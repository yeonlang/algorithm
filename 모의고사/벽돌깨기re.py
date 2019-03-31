import sys
sys.stdin = open("벽돌깨기.txt","r")
from copy import deepcopy

def issafe(y,x): return True if 0<=y<N and 0<=x<M else False
# 벽돌 깨트리기
def clr(start_x,data):
    start_y = 0
    while not data[start_y][start_x]:
        start_y+=1

    if data[start_y][start_x] == 1:
        data[start_y][start_x] = 0
        return data

    stack = [(start_y,start_x,data[start_y][start_x]-1)]
    data[start_y][start_x] = 0

    while stack:
        y,x,value = stack.pop()
        for dy,dx in (0,1),(1,0),(0,-1),(-1,0):
            ny = y
            nx = x
            for i in range(value):
                ny+=dy
                nx+=dx
                if issafe(ny,nx) and data[ny][nx]:
                    temp = data[ny][nx]
                    data[ny][nx] = 0
                    if temp>1:
                        stack.append((ny,nx,temp-1))
    return data

# 벽돌 정렬하기
def read(x,data):
    data = clr(x,data)

    for x in range(M):
        temp = []
        for y in range(N):
            if data[y][x]:
                temp.append(data[y][x])
                data[y][x] = 0
        for y in range(N-1,-1,-1):
            if temp:
                data[y][x] = temp.pop()
            else:
                break
    return data

#벽돌 떨어뜨릴 곳 정하기(중복 순열)
def BTK(c,data):
    global myMin
    # 구슬을 다 떨어뜨렸다면
    if c == K:
        # 남아있는 벽돌 수 세기
        cnt = 0
        for y in range(N):
            for x in range(M):
                if data[y][x]:
                    cnt+=1
        if cnt<myMin:
            myMin = cnt
        return

    # 벽돌이 모두 깨졌는지 확인
    for x in range(M):
        if data[N-1][x] == 0:
            if x == M-1:
                myMin = 0
                return
            continue
        else:
            break

    # 다음 떨어뜨릴 구슬 위치 정하기
    for x in range(M):
        if data[N-1][x] != 0:
            BTK(c+1,read(x,deepcopy(data)))

for tc in range(int(input())):
    K, M, N = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    myMin = M*M
    BTK(0,data)
    print("#{} {}".format(tc+1,myMin))

