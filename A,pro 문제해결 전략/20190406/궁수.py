# N,M,D 인풋
# 맨아래 성벽은 N에 포함되지 않는다.
# 1.먼저 조준을 시작한다. 적과 궁수의 거리가 D이하일때만 쏠 수 있다.
# 2.궁수는 가장 가까운 적을 쏘지만 거리가 같은 적이 여러명일 경우 왼쪽의 적을 쏜다.
# 3.같은 적을 조준하는 것도 가능하다.
# 4.적이 죽은 후에는 모든 적병이 y축으로 1칸씩 내려온다.
# 5.성벽에 닿은 적은 성벽을 올라간다.(죽은 횟수에 추가 x)
# 시간이 흘러 적병이 남지 않았을때까지 1~5 과정을 반복한다.
# 궁수를 성벽에 3명 배치할 수 있을때 가장 많이 죽일 수 있는 적병의 수를 출력한다.

import sys
sys.stdin = open("궁수.txt")

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

for tc in range(int(input())):
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
    print("#{} {}".format(tc+1,myMax))
