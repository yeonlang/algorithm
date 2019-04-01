import sys
sys.stdin = open("최소신장트리.txt")

from collections import defaultdict
INF = 99999

for tc in range(int(input())):
    dic = defaultdict(lambda :[])
    N,M = map(int,input().split())
    for _ in range(M):
        n1,n2,val = map(int,input().split())
        dic[n1].append((n2,val))
        dic[n2].append((n1,val))
    N += 1
    key = [INF]*N
    pi = [None]*N
    visited = [False]*N
    key[0] = 0

    for _ in range(N):
        myMinidx = -1
        myMin = INF
        for i in range(N):
            if not visited[i] and key[i]<myMin:
                myMin = key[i]
                myMinidx = i
        visited[myMinidx] = True
        for v,val in dic[myMinidx]:
            if not visited[v] and val<key[v]:
                key[v] = val
                pi[v] = myMinidx

    print("#{} {}".format(tc+1,sum(key)))

