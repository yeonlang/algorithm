def scale(now, right, left, x):
    if left<right:
        return 0
    if now==n:
        return 1
    if dp[x]!=-1:
        return dp[x]

    temp = 0
    for i in range(n):
        if used[i]==0:
            used[i] = 1
            temp += scale(now+1, right, left+w[i], x+(1<<i))
            temp += scale(now+1, right+w[i], left, x+(1<<(i+n)))
            used[i] = 0

    dp[x] = temp
    return temp


for t in range(int(input())):
    n = int(input())
    w = list(map(int, input().split()))
    used = [0]*n
    dp = [-1]*(1<<2*n)
    cnt = scale(0, 0, 0, 0)

    print('#{} {}'.format(t+1, cnt))