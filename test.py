n, k = map(int, input().split())
current = [k]
num = 0

if n >= k:
    print(str(n-k))
else:
    visit = [0] * 100001
    while current:
        t = current.pop(0)
        if t == n:
            break
        if t % 2 == 0 and visit[t // 2] == 0:
            current.append(t // 2)
            visit[t // 2] = visit[t] + 1
        if t - 1 >= 0 and visit[t - 1] == 0:
            current.append(t - 1)
            visit[t - 1] = visit[t] + 1
        if t + 1 < 100001 and visit[t + 1] == 0:
            current.append(t + 1)
            visit[t + 1] =visit[t]+1
    print(visit[n])