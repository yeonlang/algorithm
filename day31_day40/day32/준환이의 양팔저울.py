import sys
sys.stdin = open("준환이의 양팔저울.txt")

from collections import defaultdict
def BTK(c):
    global result
    if c == N: return 1
    templ = sorted(left)
    tempr = sorted(right)
    if dp[c][tuple(templ)][tuple(tempr)]!=0:
        return dp[c][tuple(templ)][tuple(tempr)]

    for i in range(N*2):
        if not left[i//2] and not right[i//2] and ((not i%2 and sum(left)+data[i//2]<=sum(right)) or (i%2 and sum(left)<=sum(right)+data[i//2])):
            if i%2:
                right[i//2] = data[i//2]
            else:
                left[i//2] = data[i//2]
            dp[c][tuple(templ)][tuple(tempr)] += BTK(c+1)
            if i%2:
                right[i//2] = 0
            else:
                left[i//2] = 0
    return dp[c][tuple(templ)][tuple(tempr)]

for tc in range(int(input())):
    N = int(input())
    data = list(map(int,input().split()))
    dp = [defaultdict(lambda: defaultdict(lambda : 0)) for _ in range(N)]
    visited = [0]*N
    right = [0]*N
    left = [0]*N

    result = BTK(0)
    print("#{} {}".format(tc+1,result))