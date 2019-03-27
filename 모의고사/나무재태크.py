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
        else:
            self.spread = False

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def spread(self):
    for i in range(8):
        ny = self.y+dy[i]
        nx = self.x+dx[i]
        if ispass(ny,nx):
            que[ny*N+nx].append(tree(ny,nx,1))

def winter():
    for y in range(N):
        for x in range(N):
            data[y][x] += plus[y][x]

dy = [-1,-1,-1, 0,0, 1,1,1]
dx = [-1, 0, 1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
plus = [list(map(int,input().split())) for _ in range(N)]
data = [ [5]*N for _ in range(N)]
que = [ []*N for _ in range(N) for _ in range(N)]
for i in range(M):
    y,x,age = map(int,input().split())
    que[N*(y-1)+(x-1)].append(tree(y-1,x-1,age))

t = 0
while t != K:
    for i in range(len(que)):
        if que[i]:
            que[i].sort(key= lambda x:x.age)
            for j in range(len(que[i])):
                que[i][j].spring()

    for i in range(len(que)):
        if que[i]:
            s = 0
            while s!= len(que[i]):
                if que[i][s].summer():
                    data[que[i][s].y][que[i][s].x] += que[i][s].age//2
                    del que[i][s]
                    continue
                s+=1
    for i in range(len(que)):
        if que[i]:
            l = len(que[i])
            for s in range(l):
                que[i][s].fall()
                if que[i][s].spread:
                    spread(que[i][s])
    winter()
    t+=1
cnt = 0
for i in range(N**2):
    if que[i]: cnt+= len(que[i])
print(cnt)




