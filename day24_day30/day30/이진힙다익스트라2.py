import sys
sys.stdin = open("최소거리.txt")

import heapq

for tc in range(int(input())):
    N, K = map(int,input().split())
    heap = []
    INF = 987654321
    heapq.heappush(heap, (0, 0))
    visited = [INF]*(N+1)
    visited[0] = 0
    data = [[0]*(N+1) for _ in range(N+1)]

    for j in range(K):
        start, end, value = map(int,input().split())
        data[start][end] = value

    while True:
        nowd, now = heapq.heappop(heap)

        for nxt in range(N+1):
            if data[now][nxt]:
                visited[nxt] = min(visited[nxt], nowd+data[now][nxt])
                heapq.heappush(heap, (visited[nxt],nxt))

        if not heap: break
    print("#{} {}".format(tc+1,visited[-1]))
