import sys
sys.stdin = open("나무재테크.txt")

from collections import deque
def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def fall(y,x):
    for i in range(8):
        ny = y+dy[i]
        nx = x+dx[i]
        if ispass(ny,nx):
            dic[(ny,nx)]+=[1]

dy = [-1,-1,-1, 0, 1, 1, 1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1,-1]
N,M,K = map(int,input().split())
dic = dict()
for y in range(N):
    for x in range(N):
        dic[(y,x)] = []

data = [[5]*N for _ in range(N)]
plus = [list(map(int,input().split())) for _ in range(N)]

for _ in range(M):
    y,x,age = map(int,input().split())
    y,x = y-1,x-1
    dic[(y,x)] += [age]

for y in range(N):
    for x in range(N):
        dic[(y,x)].sort(reverse=True)
        dic[(y,x)] = deque(dic[(y,x)])

spread = []
spreadin = spread.append
spreadout = spread.pop
time = 0
while time != K:
    # 봄
    for y in range(N):
        for x in range(N):
            temp = deque()
            dead=0
            while dic[(y,x)]:
                age = dic[(y,x)].pop()
                if data[y][x]-dead < age:
                    data[y][x] += age//2
                    dead += age//2
                else:
                    data[y][x] -= age
                    if age%5 == 4:
                        spreadin((y,x))
                    temp.appendleft(age+1)
            dic[(y,x)] = temp

    while spread:
        y,x = spreadout()
        fall(y,x)

    # 겨울
    for y in range(N):
        for x in range(N):
            data[y][x]+=plus[y][x]
    time+=1

cnt = 0
for y in range(N):
    for x in range(N):
        cnt+=len(dic[(y,x)])
print(cnt)









