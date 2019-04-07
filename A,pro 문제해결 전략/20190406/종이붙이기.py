import sys
sys.stdin = open("종이붙이기.txt")

def read(sy,sx,val,tp):
    for y in range(sy,sy+val):
        for x in range(sx,sx+val):
            if not tpdata[y][x]:
                return False
            else:
                tp.append((y,x))
    return True

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
                temp = []
                if read(y,x,val,temp):
                    op[val]-=1
                    for u,v in temp:
                        tpdata[u][v] = 0
                    DFS(c+1)
                    if flag:
                        return
                    for u,v in temp:
                        tpdata[u][v] = 1
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
                        candidate.append((0,n1,n2,n3,n4,n5))
myMin = -1
flag = False
candidate.sort(key = lambda x: sum(x))
for temp in candidate:
    tpdata = []
    for i in range(N):
        tpdata.append(data[i])
    op = list(temp)
    DFS(0)
    if flag:
        break
print(myMin)
