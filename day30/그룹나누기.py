import sys
sys.stdin = open("그룹나누기.txt")

class People:
    def __init__(self,i):
        self.id = i
        self.set = {i}

for tc in range(int(input())):
    N, M = map(int,input().split())
    data = list(map(int,input().split()))
    que = [0]
    for i in range(1,N+1):
        que.append(People(i))

    for j in range(M):
        a,b = data[j*2], data[j*2+1]
        que[a].set|=que[b].set
        for i in que[a].set:
            que[i] = que[a]

    result = set()
    for i in range(1,N+1):
        result.add(que[i].id)

    print("#{} {}".format(tc+1,len(result)))



