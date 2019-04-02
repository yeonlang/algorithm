import sys
sys.stdin = open("웜바이러스.txt")

class birus:
    def __init__(self,id):
        self.id = id
        self.mom = self

    def findset(self):
        if self.mom == self: return self
        self.mom = self.mom.findset()
        return self.mom

def union(x,y):
    if x.mom == data[1]:
        y.findset().mom = x.findset()
    else:
        x.findset().mom = y.findset()

N = int(input())
M = int(input())
data = [0]*(N+1)
for i in range(1,N+1):
    data[i] = birus(i)
for _ in range(M):
    x,y = map(int,input().split())
    union(data[x],data[y])
    for i in range(N):
        data[i+1].findset()

cnt = -1
for i in range(1,N+1):
    if data[i].mom == data[1]:
        cnt+=1
print(cnt)





