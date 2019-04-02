import sys
sys.stdin = open("준환이의 양팔저울.txt")

def dfs(k, used, state, left, right):  # 0:초기값 1:왼쪽 2:오른쪽
    if left<right:
        return 0
    if k==N:
        return 1
    if dp[state]!=-1:
        return dp[state]
    mySum = 0
    for i in range(N):
        bit = 1<<i
        if used&bit:
            continue
        shift = bit<<i
        mySum += dfs(k+1, used|bit, state|shift, left+data[i], right)
        mySum += dfs(k+1, used|bit, state|(shift<<1), left, right+data[i])
    dp[state] = mySum
    return mySum

T = int(input())
for tc in range(T):
    ans = 0
    N = int(input())
    data = list(map(int, input().split()))
    dp = [-1]*(1<<N*2)
    ans = dfs(0, 0, 0, 0, 0)
    print("#%d %d"%(tc+1, ans))


# def find(n, k, lw, rw, ld, rd):
#     global cnt
#     if (lw<rw):
#         return 0
#     if (n==k):
#         return 1
#     elif (d[ld][rd]!=-1):
#         return d[ld][rd]
#     else:
#         sum = 0
#         for i in range(k):
#             if (u[i]==0):
#                 u[i] = 1
#                 p[n] = i
#                 sum += find(n+1, k, lw+w[i], rw, ld+(1<<i), rd)
#                 sum += find(n+1, k, lw, rw+w[i], ld, rd+(1<<i))
#                 u[i] = 0
#         d[ld][rd] = sum
#         return sum
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     w = list(map(int, input().split()))
#     rs = sum(w)
#     p = [0]*N
#     u = [0]*N
#
#     d = [[-1]*(2**(N+1)) for i in range(2**(N+1))]
#     cnt = find(0, N, 0, 0, 0, 0)
#     print('#{} {}'.format(tc, cnt))
