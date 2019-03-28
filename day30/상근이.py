import sys
sys.stdin = open("상근이.txt")

class friend:
    def __init__(self,idx):
        self.id = idx
        self.set = set()

for tc in range(int(input())):
    N,M = map(int,input().split())
    que = [0]*(N+1)
    for i in range(1,N+1):
        que[i] = friend(i)

    for j in range(M):
        a,b = map(int,input().split())
        que[a].set.add(que[b])
        que[b].set.add(que[a])

    result = set()
    result |= que[1].set
    for i in que[1].set:
        result|=i.set

    print("#{} {}".format(tc+1,len(result)-1 if result else 0))

