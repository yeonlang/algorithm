import sys
sys.stdin = open("연구소.txt")

def read():
    stack = birus[:]
    while stack:
        now = stack.pop()
        for i in range(4):
            ny = now//M + dy[i]
            nx = now%M + dx[i]
            if 0<=ny<N and 0<=nx<M and not data[ny][nx]:
                data[ny][nx] = 3
                stack.append(nx+ny*M)
    cnt = 0
    for y in range(N):
        for x in range(M):
            if data[y][x] == 3:
                data[y][x] = 0
                cnt+=1
    return cnt

def BTK(choice, idx):
    global myMin

    if choice == 3:
        temp = read()
        if temp < myMin:
            myMin = temp
        return

    for i in range(idx,N*M):
        if data[i//M][i%M] == 0 :
            data[i//M][i%M] = 1
            BTK(choice+1,i+1)
            data[i//M][i%M] = 0

dy = [1,-1,0,0]
dx = [0,0,1,-1]

N,M = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(N)]
birus = []
result = M*N-3
for i in range(N*M):
    if data[i//M][i%M] == 2:
        birus.append(i)
        result -= 1
    elif data[i//M][i%M] == 1:
        result -= 1

myMin = 987654321
BTK(0,0)

print(result-myMin)