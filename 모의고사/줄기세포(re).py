import sys
sys.stdin = open("줄기세포.txt")

class Cell:
    num = 0
    def __init__(self,y,x,value):
        Cell.num+=1
        self.y = y
        self.x = x
        self.life = value*2
        self.value = value

    def __del__(self):
        Cell.num -= 1

def read(t):
    stack = []
    u=0
    while u != len(que):
        y = que[u][0]
        x = que[u][1]
        if data[y][x] and data[y][x] != 1:
            if data[y][x].life <= data[y][x].value:
                stack.append((y,x,data[y][x].value))

            data[y][x].life -= 1
            if data[y][x].life == 0:
                data[y][x] = 1
                que.pop(u)
                continue
        u+=1

    stack.sort(key = lambda x : x[2])
    while stack:
        y,x,value = stack.pop(0)
        for i in range(4):
            ny = y+dy[i]
            nx = x+dx[i]
            if not data[ny][nx]:
                data[ny][nx] = Cell(ny,nx,value)
                que.append((ny,nx))

# 상우하좌
dy = [-1,0,1,0]
dx = [0,1,0,-1]

for tc in range(int(input())):
    N,M,K = map(int,input().split())
    offset = K+1
    lm = M + 2 * offset
    ln = N + 2 * offset
    que = []
    stack = []
    data = [[0] * lm for _ in range(ln)]
    for i in range(N):
        for j, value in enumerate(map(int, input().split())):
            if value :
                cell = Cell(offset+i,offset+j,value)
                que.append((offset+i,offset+j))
                data[offset+i][offset+j] = cell

    t = 0
    while t!=K:
        read(t)
        t+=1

    print("#{} {}".format(tc+1,len(que)))

    # 1 22
    # 2 36
    # 3 90
    # 4 164
    # 5 712


