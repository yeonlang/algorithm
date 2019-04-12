import sys
sys.stdin = open("종이붙이기.txt")

def fill(sy,sx,val,num):
    for y in range(sy,sy+val):
        for x in range(sx,sx+val):
            data[y][x] = num

def read(sy,sx,val):
    for y in range(sy,sy+val):
        for x in range(sx,sx+val):
            if y>=N or x>=N or not data[y][x]:
                return False
    return True

def DFS(c,cnt):
    global myMin
    if c>=myMin:
        return

    if cnt == findcnt:
        if c<myMin:
            myMin = c
        return

    for y in range(N):
        for x in range(N):
            if data[y][x]:
                for val in range(5,0,-1):
                    if read(y,x,val) and op[val]:
                        op[val]-=1
                        fill(y,x,val,0)
                        DFS(c+1,cnt+val**2)
                        fill(y,x,val,1)
                        op[val]+=1
                return

op = [0,5,5,5,5,5]
N = 10
data = [list(map(int,input().split())) for _ in range(N)]
myMin = 987654321
visited = [[0]*100 for _ in range(100)]
findcnt = 0
for y in range(N):
    for x in range(N):
        if data[y][x]:
            findcnt+=1

candidate = []
for n1 in range(6):
    for n2 in range(6):
        for n3 in range(6):
            for n4 in range(6):
                for n5 in range(6):
                    if n1*(1**2) + n2*(2**2) + n3*(3**2) + n4*(4**2) + n5*(5**2) == findcnt:
                        candidate.append([0,n1,n2,n3,n4,n5])

myMin = 26
flag = False
candidate.sort(key = lambda x: sum(x))
for op in candidate:
    if sum(op)<myMin:
        DFS(0,0)
    else:
        break
if myMin == 26:
    print(-1)
else:
    print(myMin)

