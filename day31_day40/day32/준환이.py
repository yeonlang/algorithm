import sys
sys.stdin = open("준환이의 양팔저울.txt")

from collections import defaultdict
def dfs(k, used, left, right):
    if sum(left)<sum(right):
        return 0
    if k==N:
        return 1
    l = tuple(sorted(left))
    r = tuple(sorted(right))
    if dp[l][r] != -1:
        return dp[l][r]

    mySum = 0
    for i in range(N):
        bit = 1<<i
        if used&bit:
            continue
        mySum += dfs(k+1, used|bit, left+[data[i]], right)
        mySum += dfs(k+1, used|bit, left, right+[data[i]])
    dp[l][r] = mySum
    return mySum

T = int(input())
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    dp = defaultdict(lambda: defaultdict(lambda : -1))
    ans = dfs(0, 0, [], [])
    print("#%d %d"%(tc+1, ans))
