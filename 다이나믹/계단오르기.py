import sys
sys.stdin = open("계단오르기.txt")


N = int(input())
data = [0] * N
for i in range(N):
    data[i] = int(input())

dp = [0]*N
for i in range(N):
    if i < 2:
        dp[i] = sum(data[:i+1])
        continue
    if i == 2:
        dp[i] = max(data[1], data[0])+data[i]
        continue
    dp[i] = max(dp[i-3]+data[i-1],dp[i-2])+data[i]

print(dp[-1])



