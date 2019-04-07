import sys
sys.stdin = open("궁수.txt")

def array(data):
    global tpp
    # tpp의 갱신이 DFS함수에 반영되도록 전역변수로 설정
    tpp = []
    # x축을 기준으로 탐색하며 y좌표를 성벽으로 당겨주고 살아있는 적군의 위치를 tpp에 다시 저장
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
    # 궁수가 동시 조준하는 경우 카운트 중복을 막기위해 set사용
    tpset = set()
    # 조건에 맞는 각 궁수의 조준하는 적을 탐색
    for i in range(3):
        #x좌표는 궁수를 배치한 select에 저장된 위치, y는 성벽에 해당하는 N-1좌표를 할당
        y,x = N-1,select[i]

        # 배열의 크기를 넘는 초기값 설정, 갱신이 되지 않을 시에는 값이 유지
        tpmax = 9999
        ty, tx = 99, 99

        # 적군의 좌표배열을 읽어온다.
        for py,px in people:
            l = abs(py-y)+abs(px-x)
            # 사거리 안에 있고, 기존에 선택한 적군의 거리와 같지만, 적군의 x좌표가 더 작다면 갱신
            if l <= D and l == tpmax and px<tx:
                ty,tx = py,px
            # 사거리 안에 있고, 기존에 선택한 가장 가까운 적군보다 더 가깝다면 갱신
            if l <= D and l < tpmax:
                tpmax = l
                ty,tx = py,px

        # 사거리 내의 적군이 선택이 되었다면(선택이 안되었다면 tp, ty가 99) 좌표를 저장
        if ty != 99 and tx!= 99:
            tpset.add((ty,tx))
    # set의 성질에 의해 중복좌표가 없기 때문에 cnt에 set의 길이를 추가
    cnt += len(tpset)
    # 죽은 적군의 좌표를 탐색하며 0으로 tpdata를 갱신
    for y,x in tpset:
        data[y][x] = 0
    return cnt

def DFS(c,idx):
    global myMax,tpp
    #궁수 3명의 위치가 선택되면
    if c == 3:
        #원래 데이터를 유지하기 위해 2차원 배열과 적군의 좌표를 복사
        tpp = people[:]
        tpdata = []
        for u in range(N):
            tpdata.append(data[u][:])
        cnt = 0
        # 남아있는 적군이 있다면(tpp에 살아있는 적군의 좌표가 저장되어 있음) 작업을 계속 수행
        while tpp:
            # 죽인적의 수를 cnt에 추가
            cnt += solve(tpdata,tpp)
            # 적군을 성벽으로 한칸 당겨오고 tpdata와 tpp를 업데이트
            array(tpdata)
        # 죽인 적군의 수가 지금까지의 최대값보다 높다면 myMax 갱신
        if cnt>myMax:
            myMax = cnt
        return

    for i in range(idx,M):
        select[c] = i
        DFS(c+1,i+1)

N,M,D = map(int,input().split())
# 적군의 정보가 있는 2차원 배열 구현
data = [list(map(int,input().split())) for _ in range(N)]
# 0으로 된 성벽의 정보를 2차원 배열에 추가해준다.
tp = [0]*M
data.append(tp)
N+=1

# people 에 적군의 좌표를 저장
people = []
for y in range(N):
    for x in range(M):
        if data[y][x]:
            people.append((y,x))

myMax = 0
# 궁수의 위치를 기록할 배열
select = [0,0,0]
# DFS로 조합 구현
DFS(0,0)
print(myMax)