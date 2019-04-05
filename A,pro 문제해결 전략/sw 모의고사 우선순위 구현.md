
# sw 모의고사 우선순위 구현 BFS

## 아기상어(백준)

```python
import sys
sys.stdin = open("아기상어.txt")

def BFS():
    global big,start_y,start_x,result,cnt
    length = 987654321
    flag = True
    fish = []
    que = [(start_y,start_x)]
    visited = [[-1] * N for _ in range(N)]
    visited[start_y][start_x] = 0

    while que:
        y,x = que.pop(0)
        if 0<data[y][x]<9 and big > data[y][x] and visited[y][x]<=length:
            fish.append((y,x))
            if flag :
                length = visited[y][x]
                flag = False

        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if 0<=nx<N and 0<=ny<N and visited[ny][nx] == -1 and data[ny][nx]<=big:
                visited[ny][nx] = visited[y][x]+1
                que.append((ny,nx))

    if fish:
        # 먹어야 할 상어의 우선순위 구현
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
    return False

dy = [-1,0,0,1]
dx = [0,-1,1,0]

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
for y in range(N):
    for x in range(N):
        if data[y][x] == 9:
            start_y = y
            start_x = x
            data[y][x] = 0

result = 0
cnt = 0
big = 2
while BFS(): pass
print(result)

```



## 줄기세포

```python
import sys
sys.stdin = open("줄기세포.txt","r")

# alive를 1씩 줄이고 다음 후보군
def func1():
    count = 0
    for y in range(ln):
        for x in range(lm):
            if alive[y][x] and alive[y][x] <= data[y][x]:
                stack.append((y, x, data[y][x]))
            if alive[y][x] :
                alive[y][x]-=1
            if alive[y][x] :
                count+=1
    return count

#줄기세포의 상태를 변화
def search():
    count = 0
    while stack:
        y,x,value = stack.pop()

        for nxt in range(4):
            ny=y+dy[nxt]
            nx=x+dx[nxt]
            if not data[ny][nx]:
                count+=1
                data[ny][nx] = value
                alive[ny][nx] = 2*value
    return count



for tc in range(int(input())):
    N, M, K = map(int,input().split())
    offset = K//2+1
    lm = M+2*offset
    ln = N+2*offset

    data = [ [0]*lm for _ in range(ln) ]
    alive = [ [0]*lm for _ in range(ln) ]

    for i in range(N):
        for j,num in enumerate(map(int,input().split())):
            data[offset+i][offset+j] = num
            alive[offset+i][offset+j] = 2*num

    #상하좌우
    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    stack = []
    time = 0
    while time != K:
        if time == K-1:
            print('hi')
        l = func1()
        if stack:
            # 증가해야 할 줄기세포의 우선순위를 구현
            stack.sort(key=lambda x: x[2])
            result = search()

        time += 1
    if l == result:
        l = 0
    print("#{} {}".format(tc+1,result+l))

```



## 차량 정비소

```python
import sys
sys.stdin = open("차량정비소.txt")

for tc in range(int(input())):
    N1, N2, people, A, B = map(int,input().split())
    power1 = [0]*N1
    table1 = [0]*N1
    power2 = [0]*N2
    table2 = [0]*N2

    data = []
    for u,value in enumerate(map(int,input().split())):
        power1[u] = value
    for u,value in enumerate(map(int,input().split())):
        power2[u] = value
    for u,value in enumerate(map(int,input().split())):
        data.append((u+1,value))
    data.sort(key=lambda x:(x[1],x[0]))

    choice1 = []
    choice2 = []
    wait1 = []
    wait2 = []
    end = []

    time = 0
    while len(end) != people:
        for num in range(N1):
            if table1[num]:
                table1[num][0]-=1
                if table1[num][0] == 0:
                    wait2.append((table1[num][1],time,num))
                    table1[num] = 0
        if wait2:
            # 정비소를 기다리는 사람들의 우선순위를 구현
            wait2.sort(key=lambda x:(x[1],x[2]))

        for num in range(N2):
            if table2[num]:
                table2[num][0]-=1
                if table2[num][0] == 0:
                    end.append(table2[num][1])
                    table2[num] = 0

        while data and data[0][1] == time:
            wait1.append(data.pop(0))
            # 접수를 기다리는 사람들의 우선순위를 구현
            wait1.sort(key=lambda x : x[0])

        while wait1:
            flag = True
            peoplenum,j = wait1.pop(0)
            for num in range(N1):
                if table1[num] == 0:
                    if num == A-1:
                        choice1.append(peoplenum)
                    table1[num] = [power1[num],peoplenum]
                    flag = False
                    break
            if flag:
                wait1.insert(0,(peoplenum,j))
                break

        while wait2:
            flag = True
            peoplenum,j,desk = wait2.pop(0)
            for num in range(N2):
                if table2[num] == 0:
                    if num == B-1 and peoplenum in choice1:
                        choice2.append(peoplenum)
                    table2[num] = [power2[num],peoplenum]
                    flag = False
                    break
            if flag:
                wait2.insert(0,(peoplenum,j,desk))
                break
        time+=1

    if choice2:
        print("#{} {}".format(tc+1,sum(choice2)))
    else :
        print("#{} {}".format(tc+1,-1))
```

