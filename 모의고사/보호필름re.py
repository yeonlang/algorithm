import sys
sys.stdin = open("보호필름.txt")

def select(y,num):
    data[y] = [num]*M

def read(c):
    global myMin
    for x in range(M):
        cnt = [1]*N
        for y in range(N-1):
            cnt[y+1]= cnt[y]+1 if data[y][x] == data[y+1][x] else 1
            if cnt[y+1]>=K:
                break
            if y == N-2 and cnt[y+1]<K:
                return
    if c<myMin:
        myMin = c

def DFS(c,idx,num):
    if c == res:
        read(c)
        return
    for y in range(idx,N):
        temp = data[y][:]
        select(y,num)
        DFS(c+1,y+1,num)
        data[y] = temp


for tc in range(int(input())):
    N,M,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    myMin = K
    res = 0
    if myMin>1:
        while res <= myMin:
            DFS(0,0,1)
            if res==myMin: break
            DFS(0,0,0)
            res +=1
    else:
        myMin = 0
    print("#{} {}".format(tc+1,myMin))

#1 2
#2 0
#3 4
#4 2
#5 2
#6 0
#7 3
#8 2
#9 3
#10 4
