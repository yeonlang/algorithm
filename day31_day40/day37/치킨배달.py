import sys
sys.stdin = open("치킨배달.txt")

def DFS(c, idx):
    global myMin
    if c == K:
        cnt = 0
        for hy,hx in house:
            tp = 100
            for u in sl:
                cy,cx = myLst[u]
                tp = min(tp,abs(hy-cy)+abs(hx-cx))
            cnt+=tp
        if cnt<myMin:
            myMin = cnt
        return

    for i in range(idx,l):
        sl[c] = i
        DFS(c+1,i+1)

N,K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]

myLst = []
house = []
for y in range(N):
    for x in range(N):
        if data[y][x] == 2:
            myLst.append((y,x))
            data[y][x] = 0
        if data[y][x] == 1:
            house.append((y,x))

l = len(myLst)
h = len(house)
sl = [0]*K
myMin = 987654321
DFS(0,0)
print(myMin)
