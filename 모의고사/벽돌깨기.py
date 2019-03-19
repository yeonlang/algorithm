import sys
sys.stdin = open("벽돌깨기.txt","r")

def mycnt(myMap):
    cnt = 0
    for y in range(H):
        for x in range(W):
            if myMap:
                cnt+=1
    return cnt


def sight(y,x,result,myMap):
    for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
        ny=y
        nx=x
        for i in range(myMap[y][x]-1):
            ny+=dy
            nx+=dx
            if 0<=ny<H and 0<=nx<W and myMap[ny][nx]:
                result.add((ny,nx))
    return result

def clr_brick(x,myMap):
    search = set()
    search.add((H-top[x],x))
    search = sight(H-top[x],x,search,myMap)
    for i,j in search:
        search = sight(i,j,search,myMap)
    return search

def arr_brick(s,myMap):
    for i,j in s:
        myMap[i][j] = 0
    for y in range(H-1):
        for x in range(W):
            if myMap[y][x] and myMap[y+1][x] == 0:
                myMap[y][x], myMap[y+1][x] = myMap[y+1][x], myMap[y][x]


def sol(tup):
    global myMin
    myMap = []
    for i in range(len(data)):
        myMap.append(data[i][:])

    for x in tup:
        search = clr_brick(x,myMap)
        arr_brick(search,myMap)

    cnt = mycnt(myMap)
    if cnt > myMin:
        myMin = cnt 


def findtop():
    for x in range(W):
        for y in range(H):
            if data[y][x]:
                top[x] = H-y
                break


for tc in range(int(input())):
    N,W,H = map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(H)]
    myMin = 987654321
    top = [-1]*W
    findtop()
    print(top)

    dx = []
    dy = []

    sol((2,2,6))

    # for a in range(W):
    #     if N == 1:
    #         sol(a)
    #         continue
    #     for b in range(W):
    #         if N == 2:
    #             sol((a,b))
    #             continue
    #         for c in range(W):
    #             if N == 3:
    #                 sol((a,b,c))
    #                 continue
    #             for d in range(W):
    #                 sol((a,b,c,d))

