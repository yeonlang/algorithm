# 1. 완전탐색(경우의 수 구현)

* 완전 탐색의 기본은 모든 경우의 수를 살펴보는 것이다. 따라서 경우의 수를 구하는 기법인 조합, 순열, 중복조합, 중복 순열, 부분집합 등의 개념이 필요하게 된다. 
* 백준의 연구소 <https://www.acmicpc.net/problem/14502>문제를 예시로 생각해보자.
* 이 문제의 핵심은 벽을 3개 세우는 모든 경우의 수를 탐색하는 것이다. 벽을 세우는 순서는 관계없기 때문에 우리는 벽을 세울수 있는 위치를 구한후 그 중 3개의 위치에 벽을 세우는 조합마다 바이러스가 어떻게 퍼지는 지를 계산하여 문제를 풀 수 있다는 접근법을 떠올릴 수 있다. 
* 따라서 처음에는 위와같은 경우의 수를 반복문과 재귀를 사용해서 구현하는 것을 익히는 것이 선행 되야한다. 아래에는 재귀로 경우의 수를 구하는 코드 예시이다.

### 조합

```python
# 조합
def combi1(c,idx):
    if c == K:
        print(result)
        return

    for i in range(idx,N):
        result[c] = i
        combi1(c+1,i+1)
        
N = 5
K = 3
data = [1,2,3,4,5]
result = [0]*K
combi1(0,0)
```



### 순열

```python
# 순열
def permu1(c):
    if c == K:
        print(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result[c] = i
            permu1(c+1)
            visited[i]=0

N = 5
K = 3
data = [1,2,3,4,5]
visited = [0]*N
result = [0]*K

permu1(0)
```



### 중복순열

```
# 중복 순열
def permu2(c):
    if c == K:
        print(result)
        return

    for i in range(N):
        result[c] = i
        permu2(c+1)
N = 5
K = 3
data = [1,2,3,4,5]
result = [0]*K
```



### 중복조합

```python
# 중복 조합
def combi2(c,idx):
    if c == K:
        print(result)
        return

    for i in range(idx,N):
        result[c] = i
        combi2(c+1,i)
N = 5
K = 3
data = [1,2,3,4,5]
result = [0]*K
combi2(0,0)
```



### 부분집합

```python
# 부분집합
def subset(c,idx):
    print(result[:c])

    if c==N:
        return

    for i in range(idx,N):
        result[c] = i
        subset(c+1,i+1)

N = 3
data = [1,2,3]
result = [0]*N
subset(0,0)
```



# 2. 이차원 좌표에서 문제조건 구현하기

### 좌표 탐색

- 2차원을 탐색할 때에는 두가지 방식이 많이 쓰인다.

- 그 중 익숙해진다면 쉽게 구현이 가능한 방식이 이동방향을 저장하는 배열을 만들어 다음 이동위치를 제어하는 것이다.

```python
가장 기본적인 dy,dx는 다음과 같다.
# 상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]
# 우하 좌하 좌상 우상
dy = [1,1,-1,-1]
dx = [1,-1,-1,1]

추가적으로 배열의 순서등을 원하는 대로 구성 한 후에 다음과 같은 작업도 가능하다.
# 상하좌우  
dy = [-1,1,0,0]
dx = [0,0,-1,1]

# 반대방향을 리턴(상->하, 하->상, 좌->우, 우->좌)
def turn(d):
    return d-1 if d%2 else d+1

# 내가 전에 왔던 좌표 구하기
yy = y-dy[d]
xx = x-dx[d]

그런데 몇몇 문제에서는 주어지는 조건에 따라 갈 수 있는 방향이 달라지는 경우가 있다. 이때 이차원 dy,dx를 통하여 다음과 같이 구현해 볼 수 있다.

백준의 파이프 문제를 예를 들면 다음과 같다. 
각 조건에 맞는 방향을 2차원 dy,dx 로 구현한다.
dy = [[0,1],[1,1],[0,1,1]]
dx = [[1,1],[0,1],[1,0,1]]

각 인덱스마다 갈 수 있는 방향의 갯수가 다르기 때문에 이것을 조절하기 위한 1차원 배열을 만들어준다.
nowdir = [2,2,3]

이렇게 갈 수 있는 방향이 특정되면 다음과 같이 현재의 방향(d)에 따라 다음 갈 방향이 어디인지 탐색할 수 있다.
for nd in range(nowdir[d]):
	ny = y+dy[d][nd]
	nx = x+dx[d][nd]
    BTK(ny,nx,nd)    
```



- 다음은 좌표를 직접 저장해서 원하는 조건에 대한 좌표만 탐색하는 것이다. 이 방식은 좌표를 업데이트 해야하는 경우도 있고, 좌표만 가지고 원하는 조건을 구현하는 것이 어려울 수 있지만, 이차원 배열을 직접 탐색하며 갱신하는 방식보다는 훨씬 좋은 시간복잡도를 구현 할 수 있고, 익숙해 진다면 빠르게 코딩이 가능하기 때문에 유용하게 사용된다.  백준 캐슬디펜스 풀이코드를 살펴보며 어떻게 사용되는지 익혀보자.

```python
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
```



### BFS 

- 완전 탐색에 있어 가장 대표적인 것은 BFS이다. 가장 가까운 거리를 구하라,  몇 시간안에 퍼지는 영역을 구하라 등 내가 시작한 위치에서의 시간,거리 등이 연관 되어 있을 때에 자주 쓰인다. 
- (단, que를 리스트로 구현하여 pop(0)를 사용하는 것은 매우 지양해야한다. 원소를 지우고 한칸씩 당겨오는데에 O(n)의 시간 복잡도가 필요하기 때문이다. 이 구현이 필요하다면 deque자료구조를 사용하도록 한다.)
- 아래에 쓰이는 코드를 보고 어떤 식으로 사용되는지 살펴보자.
- SWEA 탈주범 검거
- 탈주범은 시간마다 연결된 파이프로 이동할 수 있다.  시간동안 이동할 수 있는 모든 위치를 구해야 하는데 이부분은 다음 칸이 연결되어 있는지 판단하는 함수만 구현한다면 BFS로 쉽게 답을 구할 수 있다.(예시 코드에서는 다 방문한 후에 visited를 세면서 count를 구하였는데 실제로는 방문해 주는 시점에 count를 +해주면서 바로 답을 구하면 시간복잡도를 낮출 수 있다. )

```python
# 내가 갈 다음위치에서 원래위치로 돌아올 수 있는지 탐색하는 함수
def judge(y,x,originy,originx):
    # 다음위치에서 이동할 수 있는칸에
    for i in range(dir_num[data[y][x]]):
        ny = y + dy[data[y][x]][i]
        nx = x + dx[data[y][x]][i]
        # 원래의 칸이 있다면 return True 아니면 False
        if ny == originy and nx == originx:
            return True
    return False

#BFS
def search(sy,sx):
    que = [(sy,sx)]
    visited[sy][sx] = 1
    while que:
        y,x = que.pop(0)
        for i in range(dir_num[data[y][x]]):
            ny = y + dy[data[y][x]][i]
            nx = x + dx[data[y][x]][i]
            # 다음 좌표가 범위 안에 위치하고, 다음 위치에 방문도 가능하며, 지금까지 방문하지 않았다면
            if 0<=ny<n and 0<=nx<m and judge(ny,nx,y,x) and not visited[ny][nx]:
                visited[ny][nx] = visited[y][x]+1
                # 거리가 K보다 커진다면 return
                if visited[ny][nx] > K:
                    return
                que.append((ny,nx))

# visited를 탐색하며 방문한 위치들을 count에 더해준다.
def solution():
    count=0
    for y in range(n):
        for x in range(m):
            if 0<visited[y][x]<=K:
                count+=1
    return count

for tc in range(int(input())):
    n,m,start_y,start_x,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(n)]
    visited = [[0]*m for _ in range(n)]
    
    # 다차원 방향좌표 설정
    # 파이프 번호에 따른 이동방향 배열로 구현
    dir_num = [0,4,2,2,2,2,2,2]
             #상하좌우,   상하,   좌우,    상우,   우하,   하좌,   좌상
    dx = [0,[0, 0, -1, 1],[0, 0], [-1, 1],[0, 1], [1, 0], [0, -1], [-1, 0]]
    dy = [0,[-1, 1, 0, 0],[-1, 1], [0, 0],[-1, 0], [0, 1], [1, 0], [0, -1]]

    search(start_y,start_x)
    print("#{} {}".format(tc+1,solution()))
```



### 우선순위 구현

* 파이썬의 sorting 함수는 일반적으로 nlogn의 시간복잡도를 가진다. 하지만 배열의 크기가 작다면 위의 시간복잡도는 의미가 없어지기 때문에 key값을 이용한 sorting으로 매우 편하게 원하는 순서대로 배열을 정렬할 수 있다. 
* 또한 복잡한 완전탐색에서 우선순위 queue를 임시로 구현하여 다음 탐색지점이나 다음 행동순서를 정한다면 문제의 깔끔한 풀이가 떠오르지 않을 때에도 답을 구현하는 데에는 성공할 수 있기 때문에 답을 구하기에는 매우 유용한 테크닉이다.  
* 깔끔하고 아름다운 방식은 아니기 때문에 아래 예시 문제를 풀어보고 필요한 부분만 받아들여 사용하도록 하자.
* 백준 아기상어( 전체코드 : <https://www.acmicpc.net/source/12337387>)

```python
# 잡아먹을 수 있는 물고기의 좌표를 fish에 저장 한 후 fish를 거리순으로, 거리가 같다면 x좌표를 기준으로 정렬 하여 잡아먹는 작업을 수행하였다. 
if fish:
    fish.sort(key=lambda x: (x[0], x[1]))
    yy, xx = fish.pop(0)
    result += visited[yy][xx]
    cnt += 1
    if cnt == big:
        cnt = 0
        big += 1
    start_y, start_x = yy, xx
    data[yy][xx] = 0
    return True
```

* 백준 색종이 붙이기

```python
candidate = []
for n1 in range(6):
    for n2 in range(6):
        for n3 in range(6):
            for n4 in range(6):
                for n5 in range(6):
                    # 색종이를 써서 만들수 있는 모든 조합으로 후보군 구성
                    if n1*(1**2) + n2*(2**2) + n3*(3**2) + n4*(4**2) + n5*(5**2) == dtcnt:
                        candidate.append([0,n1,n2,n3,n4,n5])
myMin = -1
flag = False
# 사용되는 색종이 갯수로 정렬
candidate.sort(key = lambda x: sum(x))
```

* 추가적으로 SWEA의 차량정비소, 줄기세포 등의 우선순위도 위와같은 방식을 응용하여 사용할 수 있다.



### 2차원 배열의 업데이트

*  벽돌을 부숴서 새롭게 배열을 정렬하거나, SWEA 활주로 문제처럼 일반적인 for문 while문을 단순사용하게 되면 구현이 까다롭게 느껴지는 경우가 있다. 
* 이때 임시적인 1차원 배열에 정보를 저장하고 그 정보만을 업데이트 하는 방식으로 조금 편하게 구현이 가능하다.

* 2048(오른쪽으로 미는 경우)

```python
def turn(data,d):
    if d == 0:
        for y in range(N):
            # 임시 배열을 만들어준다.
            temp = []
            # 임시 배열에 정보를 append 한 후 data 배열은 0으로 초기화한다
            for x in range(N):
                if data[y][x]:
                    temp.append(data[y][x])
                    data[y][x] = 0
			
            # while문을 돌면서 temp배열에 같은 숫자는 합쳐준다.
            i = len(temp)-1
            while 0<i:
                if temp[i] == temp[i-1]:
                    temp[i] = temp[i]+temp[i-1]
                    del temp[i-1]
                    i-=1
                i-=1
			# 합쳐진 값으로 data배열을 업데이트 한다.
            x = N-1
            while temp:
                data[y][x] = temp.pop()
                x-=1
```

* cnt 배열 사용

```python
for x in range(M):
    # 1로 초기화 된 배열을 생성
    cnt = [1]*N
    for y in range(N-1):
        # data[y+1][x]가 data[y][x] 와 같다면 cnt[y+1]은 cnt[y]+1 아니라면 1 
        cnt[y+1]= cnt[y]+1 if data[y][x] == data[y+1][x] else 1
       	# 현재 셀이 성능검사를 통과했다면 다음 셀 검사
    	if cnt[y+1]>=K:
            break
        # 통과하지 못했다면 return
        if y == N-2 and cnt[y+1]<K:
            return
# 모든 셀이 성능 검사를 통과하였고 현재 주입한 약품의 횟수가 이전 Min값보다 작다면 Min값 갱신
if c<myMin:
    myMin = c
```

# 3. 백트래킹

* 완전 탐색의 경우 순열 조합 등의 여러가지 경우의 수를 따져보게 된다. 이때 백트래킹을 사용하는 것이 주요 전략이라고 할 수 있는데 그 이유는 다음과 같다.

1. 순열의 시간복잡도가 제한시간을 초과할 때 가지치기를 사용하여 이용하여 탐색시간을 줄일 수 있다.
2. DP를 함께 구현하기에 용이하며 재귀를 이용하기 때문에 코드에 적용하기가 쉽다.
3. 조건이 시시각각 변할때 조건의 변화를 재귀함수에 넣어서 현재상태를 같이 표현할 수 있다.
4. 재귀를 이용하기 때문에 코드가 짧고, 구조를 파악하기가 쉽다.
  (특히 삼성의 경우 제한 시간을 여유롭게 주기 때문에 아무 생각없이 익숙하게 구현만 해도 맞는 경우가 많다.)

*  다만 빠르게 구성하였는데 답이 틀리게 나오고 경우의 수가 너무 복잡할 경우 백트래킹은 디버깅이 힘들 수 있기 때문에 시간복잡도를 생각해보고 완전탐색이 가능하다면 stack이나 queue를 쓰는 BFS,DFS로 빠르게 변경해 보는 것도 좋다.
* 프로세서 연결을 대상으로 어떻게 코어를 선택하고 상태의 변화를 저장할 수 있는지 살펴보자.

### 프로세서연결

```python
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
```

### 보호필름

```python
# 약품처리된 셀을 num로 바꿔주는 함수
def select(y,num):
    data[y] = [num]*M

# 성능검사
def read(c):
    global myMin
    for x in range(M):
        cnt = [1]*N
        for y in range(N-1):
            cnt[y+1]= cnt[y]+1 if data[y][x] == data[y+1][x] else 1
            # 성능검사를 통과하였다면 다음 x축 성능검사로 넘어감
            if cnt[y+1]>=K:
                break
            # 하나라도 못 통과하였다면 return
            if y == N-2 and cnt[y+1]<K:
                return
    # 모든셀이 성능검사를 통과하였다면 myMin을 갱신
    if c<myMin:
        myMin = c

def DFS(c,idx,num):
    #약품처리가 원하는 횟수만큼 되었다면 작업 개시
    if c == res:
        # 성능검사를 통과하는지 살펴본다.
        read(c)
        return
    # 약품처리를 해줘야 할 셀을 선택(조합)
    for y in range(idx,N):
        # 약품처리 전 상태를 temp에 저장
        temp = data[y][:]
        # 약품처리 후 다음 약품 처리할 위치를 탐색
        select(y,num)
        DFS(c+1,y+1,num)
        # 다시 약품을 처리하지 않았을 상태로 복귀
        data[y] = temp


for tc in range(int(input())):
    N,M,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    myMin = K
    res = 0
    if myMin>1:
        while res <= myMin:
            # 1로 약품처리르 하였을 경우
            DFS(0,0,1)
            if res==myMin: break
            # 0으로 약품처리를 하였을 경우
            DFS(0,0,0)
            res +=1
    else:
        myMin = 0
    print("#{} {}".format(tc+1,myMin))
```

ex: 등산로조성, 숫자만들기, 연구소(백준), 디저트카페, 요리사, 감시(백준) 등

# 4. 시뮬레이션

* 큐브를 돌린다거나(큐빙) 좌표값에 2개 이상의 정보가 담기는 경우, 현재 정보를 바탕으로 부딪치고 소멸하고 합쳐지는 작업들이 달라지는 경우에는 클래스를 사용하는 것이 좋다. 
* 파이썬은 리스트에 클래스 인스턴트를 담을 수 있고, 그것을 이용하여 어떤 조건이 만족되었을 시에 각 인스턴트 내부의 정보를 업데이트 하는 것이 실제 시뮬레이션을 하는데 있어 매우 유리하기 때문이다.

### 주사위굴리기(백준)

```python

def issafe(y,x) : return True if 0<=y<N and 0<=x<M else False
def trans(d):
    if d == 0:
        cube.top,cube.left,cube.bottom,cube.right = cube.left,cube.bottom,cube.right,cube.top
    elif d == 1:
        cube.top, cube.left, cube.bottom, cube.right = cube.right, cube.top, cube.left, cube.bottom
    elif d == 2:
        cube.top,cube.front,cube.bottom,cube.back = cube.front,cube.bottom,cube.back,cube.top
    elif d == 3:
        cube.top,cube.front,cube.bottom,cube.back = cube.back,cube.top,cube.front,cube.bottom

class cube:
    def __init__(self,value):
        self.value = value

cube.left = cube(0)
cube.right = cube(0)
cube.bottom = cube(0)
cube.top = cube(0)
cube.front = cube(0)
cube.back = cube(0)

N,M,y,x,K = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
direct = list(map(lambda x: int(x)-1,input().split()))
    #우좌상하
dy = [0,0,-1,1]
dx = [1,-1,0,0]

for i in direct:
    ny=y+dy[i]
    nx=x+dx[i]
    if issafe(ny,nx):
        trans(i)
        y = ny
        x = nx
        if data[y][x]:
            cube.bottom.value = data[y][x]
            data[y][x] = 0
        else:
            data[y][x] = cube.bottom.value
        print(cube.top.value)
```



### 줄기세포

```python
class Cell:
    def __init__(self,y,x,value):
        self.y = y
        self.x = x
        self.life = value*2
        self.value = value
        self.spread = False

def spread():
    que.sort(key = lambda x : x.value,reverse = True)
    i = 0
    while i != len(que):
        y,x,value = que[i].y,que[i].x,que[i].value
        for u in range(4):
            ny = y+dy[u]
            nx = x+dx[u]
            if not data[ny][nx] and que[i].spread:
                data[ny][nx] = que[i].value
                que.append(Cell(ny,nx,value))
        if que[i].spread: que[i].spread = False
        i+=1

def read():
    i = 0
    while i != len(que):
        if que[i].life == que[i].value:
            que[i].spread = True
        que[i].life -= 1
        if que[i].life < 0:
            del que[i]
            continue
        i+=1

# 상우하좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]

for tc in range(int(input())):
    N,M,K = map(int, input().split())

    offset = K // 2 + 1
    lm = M + 2 * offset
    ln = N + 2 * offset
    que = []
    data = [[0] * lm for _ in range(ln)]
    for i in range(N):
        for j, value in enumerate(map(int, input().split())):
            if value :
                que.append(Cell(offset+i,offset+j,value))
                data[offset+i][offset+j] = value

    t = 0
    while t != K:
        read()
        spread()
        t+=1
    read()

    print("#{} {}".format(tc + 1, len(que)))
```







