import sys
sys.stdin = open("최소거리.txt")

def func():
    cnt = 10000
    for i in range(N):
        if (cnt == 10000 or distance[i][0]<distance[cnt][0]) and not distance[i][1]:
            if cnt == 10000:
                cnt = i
                continue
            if distance[i][0]<distance[cnt][0]:
                cnt = i
    if cnt == 10000:
        return (0, True)
    return (cnt, False)

for tc in range(int(input())):
    N, K = map(int,input().split())
    heap = []
    INF = 10000
    distance = [[INF, 0] for _ in range(N+1)]
    data = [[0]*(N+1) for _ in range(N+1)]

    start = 0
    distance[start][0] = 0

    for j in range(K):
        start, end, value = map(int,input().split())
        data[start][end] = value

    while True:
        now, flag = func()
        if flag: break
        distance[now][1] = 1
        for nxt in range(N+1):
            if data[now][nxt]:
                distance[nxt][0] = min(distance[nxt][0],distance[now][0] + data[now][nxt])

    print("#{} {}".format(tc+1,distance[-1][0]))

