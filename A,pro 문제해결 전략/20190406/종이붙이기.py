import sys
sys.stdin = open("종이붙이기.txt")

def read(sy,sx,val):
    for y in range(sy,sy+val):
        for x in range(sx,sx+val):
            if not data[y][x]:
                return False
    return True

def fill(sy,sx,val,num):
    for y in range(sy,sy+val):
        for x in range(sx,sx+val):
            data[y][x] = num

def DFS(c):
    global myMin,flag
    if op[1] == op[2] == op[3] == op[4] == op[5] == 0:
        myMin = c
        flag = True
        return

    for val in range(5,0,-1):
        if not op[val]:
            continue
        for y in range(N-val+1):
            for x in range(N-val+1):
                if read(y,x,val):
                    op[val]-=1
                    fill(y,x,val,0)
                    DFS(c+1)
                    if flag:
                        return
                    fill(y,x,val,1)
                    op[val]+=1
        return

N = 10
data = [list(map(int,input().split())) for _ in range(N)]
dtcnt = 0
for y in range(N):
    for x in range(N):
        if data[y][x]:
            dtcnt+=1

candidate = []
for n1 in range(6):
    for n2 in range(6):
        for n3 in range(6):
            for n4 in range(6):
                for n5 in range(6):
                    if n1*(1**2) + n2*(2**2) + n3*(3**2) + n4*(4**2) + n5*(5**2) == dtcnt:
                        candidate.append([0,n1,n2,n3,n4,n5])
myMin = -1
flag = False
candidate.sort(key = lambda x: sum(x))
for op in candidate:
    DFS(0)
    if flag:
        break
print(myMin)
