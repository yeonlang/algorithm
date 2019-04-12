def select(enemy):
    s = set()
    for c in range(3):
        x = result[c]
        y = N
        tmax,ty,tx = 9999,99,99
        for i in range(len(enemy)):
            py,px = enemy[i][0],enemy[i][1]
            l = abs(y-py) + abs(x-px)
            if l<=D and l<tmax:
                tmax = l
                ty, tx = py, px
                idx = i
            if l<=D and l == tmax and px<tx:
                ty, tx = py, px
                idx = i
        if tmax != 9999:
            s.add(idx)

    temp = list(s)
    temp.sort(reverse = True)
    for u in temp:
        del enemy[u]
    return len(s)

def array(enemy):
    i = 0
    while i<len(enemy):
        enemy[i][0] += 1
        if enemy[i][0] == N:
            del enemy[i]
            continue
        i+=1

def DFS(c,idx):
    global myMin
    if c == 3:
        enemy = [x[:] for x in people]
        cnt = 0
        while enemy:
            cnt+=select(enemy)
            array(enemy)
        if cnt>myMin:
            myMin = cnt
        return

    for i in range(idx,M):
        result[c] = i
        DFS(c+1,i+1)

N,M,D = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
people = []
for y in range(N):
    for x in range(M):
        if data[y][x]:
            people.append([y,x])

result = [0,0,0]
myMin = 0
DFS(0,0)
print(myMin)