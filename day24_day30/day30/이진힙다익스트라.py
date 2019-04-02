import sys
sys.stdin = open("최소거리.txt")

import heapq
from collections import defaultdict

for tc in range(int(input())):
    N, K = map(int,input().split())
    heap = []
    INF = 987654321
    heapq.heappush(heap, (0, 0))
    visited = [INF]*(N+1)
    visited[0] = 0

    dic = defaultdict(lambda : [])
    for i in range(1,N+1):
        heapq.heappush(heap, (INF,i))

    for j in range(K):
        start, end, value = map(int,input().split())
        dic[start].append((end,value))

    while True:
        nowd, now = heapq.heappop(heap)
        if nowd == INF: break
        for idx,d in dic[now]:
            visited[idx] = min(visited[idx], nowd+d)
            heapq.heappush(heap, (visited[idx],idx))

    print("#{} {}".format(tc+1,visited[-1]))


