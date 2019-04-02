import sys
sys.stdin = open("계단오르기.txt")

N = int(input())
data = [0] * N
for i in range(N):
    data[i] = int(input())

dp = [[0]*2 for _ in range(N)]
dp[0][0] = data[0]
dp[0][1] = 0
dp[1][0] = data[1]
dp[1][1] = data[1]+data[0]
for i in range(2,N):
    dp[i][0] = max(dp[i-2][0],dp[i-2][1]) + data[i]
    dp[i][1] = dp[i-1][0] + data[i]

print(max(dp[N-1][0],dp[N-1][1]))





