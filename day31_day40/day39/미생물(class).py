import sys
sys.stdin = open("미생물.txt")

class Cell:
    def __init__(self,y,x,num,d):
        self.maxnum = num
        self.y = y
        self.x = x
        self.num = num
        self.d = d

def turn(cell):
    if cell.d % 2:
        cell.d-=1
    else:
        cell.d+=1
    cell.num //= 2

    #상하좌우
dy = [-1,1,0,0]
dx = [0,0,-1,1]

for tc in range(int(input())):
    N, time, K = map(int,input().split())
    data = []
    for _ in range(K):
        y, x, num, d = map(int,input().split())
        data.append(Cell(y,x,num,d-1))

    t = 0
    while t != time:
        visited = dict()
        i = 0
        while i<len(data):
            cell = data[i]
            cell.y+=dy[cell.d]
            cell.x+=dx[cell.d]
            if cell.y == 0 or cell.y == N-1 or cell.x == 0 or cell.x == N-1:
                turn(cell)
            if (cell.y,cell.x) in visited.keys():
                precell = visited[(cell.y,cell.x)]
                if cell.num>precell.maxnum:
                    precell.maxnum = cell.num
                    precell.d = cell.d
                precell.num += cell.num
                data.pop(i)
                continue
            visited[(cell.y,cell.x)] = cell
            i+=1
        for cell in visited.values():
            cell.maxnum = cell.num
        t+=1

    ans = 0
    for cell in data:
        ans+=cell.num
    print("#{} {}".format(tc+1,ans))
