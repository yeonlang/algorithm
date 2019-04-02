def btk(start, nowsum):
    global minsum, visited
    road.append(start)

    if len(road) == 1:
        nowsum += weight[0][start + 1]

    if len(road) >= n:
        nowsum += weight[start + 1][1]
        if nowsum < minsum:
            minsum = nowsum

        nowsum -= weight[start + 1][1]
        return

    if nowsum > minsum:
        return

    for nxt in range(1, n + 1):
        if weight[start + 1][nxt + 1] and not visited[nxt]:
            nowsum += weight[start + 1][nxt + 1]
            visited[start] = 1
            btk(nxt, nowsum)
            nowsum -= weight[start + 1][nxt + 1]
            road.pop()
            visited[nxt] = 0


for tc in range(int(input())):
    n = int(input())
    data = list(map(int, input().split()))
    weight = [[0] * (n + 2) for _ in range(n + 2)]
    minsum = 987654321

    for start in range(n + 2):
        for end in range(n + 2):
            weight[start][end] = abs(data[2 * start] - data[2 * end]) + abs(data[2 * start + 1] - data[2 * end + 1])
    for start in range(1, n + 1):
        road = []
        visited = [0] * (n + 1)
        btk(start, 0)
    print("#{} {}".format(tc+1,minsum))