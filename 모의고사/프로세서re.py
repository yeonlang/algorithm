import sys
sys.stdin = open("엑시노스.txt")

# 코어의 상하좌우를 탐색하며 연결 가능한 전선을 찾는 함수
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
    # 원하는 만큼 코어를 선택할 수 있었다면 작업 수행(K는 아래 main부분의 res를 뜻한다.)
    if c == K:
        if cnt<myMin:
            myMin = cnt
        return

    # core[c]에는 현재 선택한 코어에서 상하좌우 연결할 수 있는 좌표값들이 저장되어 잇다.
    for i in core[c]:
        # 현재의 상태(myset,cnt)를 유지하기 위해  nxtcnt, nxtset을 새롭게 만들어준다.
        nxtcnt = cnt+len(i)
        nxtset = myset|i
        #내가 선택한 방향의 전선이 다른 전선과 겹치는 부분이 있다면 가지치기
        if nxtcnt != len(nxtset): continue
        # 겹치는 부분이 없었다면 다음 코어를 선택하기 위해 넘어간다.
        BTK(c+1,K,nxtset,nxtcnt)

dy = [-1,0,1,0]
dx = [0,1,0,-1]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    INF = 987654321

    # 각 코어에서 상하좌우 연결이 가능 한 곳이라면 튜플(y,x) 형태로 set을 만들어 core에 저장한다.
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
    # 코어를 전체 다 사용해서 만들수 있는지부터 시작해서 res를 감소시켜주며 탐색
    while res:
        flag = False
        myMin = INF
        BTK(0,res,set(),0)
        # 코어를 사용해서 만들수 있는 경우가 생겼다면 break
        if myMin != INF:
            break
        res-=1
    print("#{} {}".format(tc+1,myMin))


