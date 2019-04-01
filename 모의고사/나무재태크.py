import sys
sys.stdin = open("나무재태크.txt")

from collections import defaultdict,deque
class tree:
    def __init__(self,age):
        self.age = age
        self.dead = False
        self.spread = False

    def spring(self,y,x):
        if data[y][x] < self.age:
            self.dead = True
        else:
            data[y][x] -= self.age
            self.age+=1

    def summer(self):
        if self.dead: return True
        else: return False

def ispass(y,x): return True if 0<=y<N and 0<=x<N else False
def spread(y,x):
    for i in range(8):
        ny = y+dy[i]
        nx = x+dx[i]
        if ispass(ny,nx):
            dic[(ny,nx)].appendleft(tree(1))

dy = [-1,-1,-1, 0,0, 1,1,1]
dx = [-1, 0, 1,-1,1,-1,0,1]
N,M,K = map(int,input().split())
plus = [list(map(int,input().split())) for _ in range(N)]
data = [ [5]*N for _ in range(N)]
dic = defaultdict(lambda :deque())

for i in range(M):
    y,x,age = map(int,input().split())
    dic[(y-1,x-1)].append(tree(age))

t = 0
while t != K:
    for y in range(N):
        for x in range(N):
            if dic[(y,x)]:
                for i in dic[(y,x)]:
                    i.spring(y,x)
                s = 0
                while s != len(dic[(y,x)]):
                    if dic[(y,x)][s].summer():
                        data[y][x] += dic[(y,x)][s].age//2
                        del dic[(y,x)][s]
                        continue
                    s+=1
    for y in range(N):
        for x in range(N):
            data[y][x] += plus[y][x]
            for i in dic[(y, x)]:
                if not i.age%5:
                    spread(y,x)
    t+=1

cnt = 0
for y in range(N):
    for x in range(N):
        cnt += len(dic[(y,x)])
print(cnt)


