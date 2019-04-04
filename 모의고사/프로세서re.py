import sys
sys.stdin = open("엑시노스.txt")

def func(y,x,d):
    s = set()
    while True:
        y+=dy[d]
        x+=dx[d]
        if data[y][x]:
            return False
        s.add((y,x))
        if y == N-1 or x == N-1 or y == 0 or x == 0:
            return s

def BTK(c,K,myset,cnt):
    global myMin,flag
    if c == K:
        if cnt<myMin:
            myMin = cnt
        return

    for i in core[c]:
        nxtcnt = cnt+len(i)
        nxtset = myset|i
        if nxtcnt != len(nxtset): continue
        BTK(c+1,K,nxtset,nxtcnt)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    INF = 987654321
    core = []
    for y in range(1,N-1):
        for x in range(1,N-1):
            if data[y][x]:
                lst = []
                for d in range(4):
                    temp = func(y,x,d)
                    if temp:
                        lst.append(temp)
                if lst:
                    core.append(lst)

    res = len(core)
    while res:
        flag = False
        myMin = INF
        BTK(0,res,set(),0)
        if myMin != INF:
            break
        res-=1
    print("#{} {}".format(tc+1,myMin))


