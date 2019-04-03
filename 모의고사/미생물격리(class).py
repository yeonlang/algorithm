import sys
sys.stdin = open("미생물.txt")

class Cell:
    def __init__(self,y,x,num,d):
        self.y = y
        self.x = x
        self.num =num
        self.d = d

def turn(cell):
    if cell.d % 2:
        cell.d-=1
    else:
        cell.d+=1

    #상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for tc in range(int(input())):
    N, time, K = map(int,input().split())
    data = [[[] for _ in range(N)] for _ in range(N)]
    for _ in range(K):
        y, x, num, d = map(int,input().split())
        data[y][x].append(Cell(y,x,num,d-1))

    t = 0
    while t != time:
        que = []
        for y in range(N):
            for x in range(N):
                if data[y][x]:
                    for cell in data[y][x]:
                        cell.y+=dy[cell.d]
                        cell.x+=dx[cell.d]
                        que.append(cell)
                    data[y][x] = []

        while que:
            cell = que.pop()
            data[cell.y][cell.x].append(cell)

        for y in range(N):
            for x in range(N):
                if data[y][x] and (y == 0 or y == N-1 or x == 0 or x == N-1):
                    cell = data[y][x][0]
                    cell.num = cell.num//2
                    turn(cell)
                elif len(data[y][x])>1:
                    data[y][x].sort(key=lambda x:x.num,reverse=True)
                    nd = data[y][x][0].d
                    cnt = 0
                    for cell in data[y][x]:
                        cnt+=cell.num
                    data[y][x] = [Cell(y,x,cnt,nd)]
        t+=1

    ans = 0
    for y in range(N):
        for x in range(N):
            for cell in data[y][x]:
                ans+=cell.num
    print("#{} {}".format(tc+1,ans))


