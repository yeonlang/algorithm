import sys
sys.stdin = open("줄기세포.txt")

class Cell:
    num = 0
    def __init__(self,y,x,value):
        Cell.num += 1
        self.y = y
        self.x = x
        self.life = value*2
        self.value = value
        self.spread = False

    def __del__(self):
        Cell.num -= 1

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

    print("#{} {}".format(tc + 1, Cell.num))




    # 1 22
    # 2 36
    # 3 90
    # 4 164
    # 5 712


