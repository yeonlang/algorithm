import sys
sys.stdin = open("엑시노스.txt","r")

from itertools import product,combinations

def func():
    global my_max
    k = len(core)
    while k:
        for i in combinations(core,k):
            for j in product(*i):
                a = sol(j)
                if a and a<my_max:
                    my_max = a
        if my_max != 987654321:
            return
        k-=1

def sol(sets):
    global my_max
    l = 0
    judge = set()
    for i in sets:
        l += len(i)
        judge |= i
        if l > my_max:
            return

    if len(judge) == l:
        return l

def sight(y0, x0):
    for dy, dx in (1,0), (-1,0), (0,1), (0,-1):
        y, x = y0+dy, x0+dx
        seen = set()
        while 0<=y<n and 0<=x<n and data[y][x] == 0:
            seen.add((y,x))
            y+= dy; x+= dx
        if (y0,0) in seen or (y0,n-1) in seen or (0,x0) in seen or (n-1,x0) in seen:
            yield seen

for tc in range(int(input())):
    n = int(input())
    data = [ list(map(int,input().split())) for _ in range(n) ]
    core = []
    result = []
    my_max = 987654321
    for y in range(1,n-1):
        for x in range(1,n-1):
            if data[y][x] :
                now_core=[]
                for root in sight(y, x):
                    now_core.append(root)
                core.append(now_core)

    func()

    print("#{} {}".format(tc+1,my_max))