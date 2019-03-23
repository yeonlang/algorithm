# sw 모의고사 백트래킹

## 숫자만들기

```python
def cal(num,cnt,choice):
    if num == 0: return cnt+data[choice+1]
    elif num == 1: return cnt-data[choice+1]
    elif num == 2: return cnt*data[choice+1]
    elif num == 3: return int(cnt/data[choice+1])

def BTK(choice,N,cnt):
    global myMax , myMin
    if choice == N-1:
        if cnt>=myMax:
            myMax = cnt
        if cnt<=myMin:
            myMin = cnt
        return

    for i in range(4):
        if operator[i]>0:
            operator[i] -= 1
            BTK(choice+1,N,cal(i,cnt,choice))
            operator[i] += 1

for tc in range(int(input())):
    N = int(input())
    visited = [0]*(N-1)
    operator = list(map(int,input().split()))
    data = list(map(int,input().split()))

    myMax = -987654321
    myMin = 987654321
    BTK(0,N,data[0])

    print("#{} {}".format(tc+1,myMax-myMin))
```



## 수영장

```python
def BTK(now):
    global cnt,minpay

    if now>11:
        if cnt<minpay:
            minpay = cnt
        return

    for i,time in enumerate([3,1,1]):
        if i == 0:
            cnt+=trimon
            BTK(now+time)
            cnt-=trimon
        elif i == 1:
            cnt+=mon
            BTK(now+time)
            cnt-=mon
        else:
            temp = day*data[now]
            cnt += temp
            BTK(now+time)
            cnt -= temp

for tc in range(int(input())):
    day, mon, trimon, minpay = map(int,input().split())
    data = list(map(int,input().split()))

    cnt = 0
    BTK(0)
    print("#{} {}".format(tc+1,minpay))
```



##  파이프(백준 통과 불가능)

```python
def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BTK(y,x,d):
    global result
    if y == N-1 and x == N-1:
        result+=1
        return
    for i in range(nowdir[d]):
        ny = y+dy[d][i]
        nx = x+dx[d][i]
        if ispass(ny,nx):
            nd = nxtdir[d][i]
            if nd == 0 and data[ny][nx] == 0: BTK(ny,nx,nd)
            elif nd == 1 and data[ny][nx] == 0: BTK(ny,nx,nd)
            elif nd == 2 and data[ny-1][nx] == 0 and data[ny][nx-1] == 0 and data[ny][nx] == 0:
                BTK(ny,nx,nd)

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
result = 0
nowdir = [2,2,3]
dy = [[0,1],[1,1],[0,1,1]]
dx = [[1,1],[0,1],[1,0,1]]
nxtdir = [[0,2],[1,2],[0,1,2]]

BTK(0,1,0)
print(result)
```



## 파이프(DP추가 백준 통과가능)

```python
def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BTK(y,x,d):
    global result
    if dp[d][y][x] != -1 : return dp[d][y][x]
    if y == N-1 and x == N-1: return 1

    dp[d][y][x] = 0

    for i in range(nowdir[d]):
        ny = y+dy[d][i]
        nx = x+dx[d][i]
        if ispass(ny,nx):
            nd = nxtdir[d][i]
            if nd == 0 and data[ny][nx] == 0:
                dp[d][y][x] += BTK(ny,nx,nd)
            elif nd == 1 and data[ny][nx] == 0:
                dp[d][y][x] += BTK(ny,nx,nd)
            elif nd == 2 and data[ny-1][nx] == 0 and data[ny][nx-1] == 0 and data[ny][nx] == 0:
                dp[d][y][x] += BTK(ny,nx,nd)

    return dp[d][y][x]

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
result = 0
dp = [[[-1]*N for _2 in range(N)] for _3 in range(3)]
nowdir = [2,2,3]
dy = [[0,1],[1,1],[0,1,1]]
dx = [[1,1],[0,1],[1,0,1]]
nxtdir = [[0,2],[1,2],[0,1,2]]

result = BTK(0,1,0)
print(result)
```



##  등산로 조성

```python
def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def BTK(y,x,flag):
    global cnt,result
    if cnt>result:
        result = cnt

    for dy,dx in (0,1),(-1,0),(0,-1),(1,0):
        ny = y+dy
        nx = x+dx
        if flag:
            if ispass(ny,nx) and not visited[ny][nx] and data[y][x]>data[ny][nx]:
                visited[ny][nx] = 1
                cnt+=1
                BTK(ny,nx,flag)
                cnt-=1
                visited[ny][nx] = 0
            elif ispass(ny,nx) and not visited[ny][nx] and data[ny][nx]-data[y][x]<K:
                temp=data[ny][nx]-data[y][x]+1
                data[ny][nx] -= temp
                visited[ny][nx] = 1
                cnt+=1
                flag=False
                BTK(ny,nx,flag)
                flag=True
                cnt-=1
                visited[ny][nx] = 0
                data[ny][nx] += temp

        else:
            if ispass(ny,nx) and not visited[ny][nx] and data[y][x] > data[ny][nx]:
                visited[ny][nx] = 1
                cnt+=1
                BTK(ny,nx,flag)
                cnt-=1
                visited[ny][nx] = 0


dy = [1,-1,0,0]
dx = [0,0,1,-1]
for tc in range(int(input())):
    N,K = map(int,input().split())
    data = [ list(map(int,input().split())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    myMax = 0
    start = []

    for ay in range(N):
        for ax in range(N):
            if data[ay][ax] > myMax:
                start = [(ay,ax)]
                myMax = data[ay][ax]
            elif data[ay][ax] == myMax:
                start.append((ay, ax))

    result = 0
    for y,x in start:
        cnt = 1
        visited[y][x]=1
        BTK(y,x,True)
        visited[y][x]=0

    print("#{} {}".format(tc+1,result))
```



## 디저트 카페

```python
def BTK(y,x,start_y,start_x,nowdir):
    global ans
    for i in range(2):
        if nowdir+i>3:
            return
        ny=y+dy[nowdir+i]
        nx=x+dx[nowdir+i]
        if ny == start_y and nx == start_x:
            if len(visited)>ans:
                ans = len(visited)

        if 0<=ny<N and 0<=nx<N and not data[ny][nx] in visited:
            visited.add(data[ny][nx])
            BTK(ny,nx,start_y,start_x,nowdir+i)
            visited.remove(data[ny][nx])

dy = [1,1,-1,-1]
dx = [1,-1,-1,1]

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    ans = -1

    for y in range(N-2):
        for x in range(N):
            visited = set([data[y][x]])
            BTK(y,x,y,x,0)

    print("#{} {}".format(tc+1,ans))

```



## 요리사

```python
def BTK(choice,idx):
    global myMin
    if choice == N//2:
        data1,data2 = [],[]
        for i in range(N):
            if visited[i] == 0:
                data1.append(i)
            else :
                data2.append(i)
        A = 0
        B = 0
        for a in data1:
            for b in data1:
                if a != b:
                    A+= data[a][b]
        for a in data2:
            for b in data2:
                if a != b:
                    B+= data[a][b]
        temp = abs(A-B)
        if temp < myMin:
            myMin = temp
        return

    for i in range(idx+1,N):
        visited[i] = 1
        BTK(choice+1,i)
        visited[i] = 0

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    myMin = 987654321

    BTK(0,-1)
    print("#{} {}".format(tc+1,myMin))
```



