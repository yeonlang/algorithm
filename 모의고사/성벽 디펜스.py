import sys
sys.stdin = open("성벽디펜스.txt")

def array(data):
    global tpp
    tpp = []
    for x in range(M):
        for y in range(N-1,0,-1):
            data[y][x] = data[y-1][x]
            if y == N-1:
                data[y][x] = 0
            data[y-1][x] = 0
            if data[y][x]:
                tpp.append((y,x))

def solve(data,people):
    cnt = 0
    tpset = set()
    for i in range(3):
        x = select[i]
        y = N-1
        tpmax = 9999
        ty, tx = 99, 99

        for py,px in people:
            l = abs(py-y)+abs(px-x)
            if l <= D and l < tpmax:
                tpmax = l
                ty,tx = py,px
            if l <= D and l == tpmax and x<tx:
                ty,tx = py,px

        if ty != 99 and tx!= 99:
            tpset.add((ty,tx))
    cnt += len(tpset)
    for y,x in tpset:
        data[y][x] = 0
    return cnt

def DFS(c,idx):
    global myMax,tpp
    if c == 3:
        cnt = 0
        tpp= people[:]
        tpdata = []
        for u in range(N):
            tpdata.append(data[u][:])

        while True:
            cnt += solve(tpdata,tpp)
            array(tpdata)
            if not tpp:
                break

        if cnt>myMax:
            myMax = cnt
        return

    for i in range(idx,M):
        select[c] = i
        DFS(c+1,i+1)

N,M,D = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
data.append([0]*M)
N+=1
people = []
for y in range(N):
    for x in range(M):
        if data[y][x]:
            people.append((y,x))
myMax = 0
select = [0,0,0]
DFS(0,0)
print(myMax)