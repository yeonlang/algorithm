import sys
sys.stdin = open("나무재태크.txt")

class tree:
    def __init__(self,y,x,age):
        self.y = y
        self.x = x
        self.age = age
        self.dead = False
        self.spread = False

    def spring(self):
        if data[self.y][self.x] < self.age:
            self.dead = True
        else:
            data[self.y][self.x] -= self.age
            self.age+=1
    def summer(self):
        if self.dead: return True
        else: return False

    def fall(self):
        if not self.age%5:
            self.spread = True

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def spread(self):
    for i in range(8):
        ny = self.y+dy[i]
        nx = self.x+dx[i]
        if ispass(ny,nx):
            que.append(tree(nx,ny,1))

def winter():
    for y in range(N):
        for x in range(N):
            data[y][x] += plus[y][x]

dy = [-1,-1,-1, 0,0, 1,1,1]
dx = [-1, 0, 1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
plus = [list(map(int,input().split())) for _ in range(N)]
data=[[5]*N for _ in range(N)]
que = []
for i in range(M):
    x,y,age = map(int,input().split())
    que.append(tree(y-1,x-1,age))


t = 0
while t != K:
    que.sort(key=lambda x: x.age)
    for i in range(len(que)):
        que[i].spring()
    s = 0
    while s!= len(que):
        if que[s].summer():
            data[que[s].y][que[s].x] += que[s].age//2
            del que[s]
            continue
        s+=1

    l = len(que)
    for i in range(l):
        que[i].fall()
        if que[i].spread:
            spread(que[i])

    winter()
    t+=1

print(len(que))




