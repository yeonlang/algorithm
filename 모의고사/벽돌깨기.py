import sys
sys.stdin = open("벽돌깨기.txt","r")

def sight(y,x,result,myMap):

    for dy,dx in (1,0),(-1,0),(0,1),(0,-1):
        ny=y
        nx=x
        for i in range(myMap[y][x]-1):
            ny+=dy
            nx+=dx
            if 0<=ny<H and 0<=nx<W and myMap[ny][nx]:
                result|=(ny,nx)

def clr_brick(x,myMap):
    search = set((H-top[x],x))
    sight(H-top[x],x,search,myMap)
    for i,j in search:
        sight(i,j,search)
    return search

def arr_brick(s):
    for y,x in s:
        myMap

def sol(tup):
    myMap = []
    for i in range(len(data)):
        myMap.append(data[i][:])

    for x in tup:
        arr_brick(clr_brick(x,myMap))

def findtop():
    for x in range(W):
        for y in range(H):
            if data[y][x]:
                top[x] = H-y
                break


for tc in range(int(input())):
    N,W,H = map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(H)]

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

