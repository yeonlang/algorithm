import sys
sys.stdin = open("RGB거리.txt")

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

dp = [[[0]*3 for _ in range(3)] for _ in range(N)]
# red = 0 green = 1 blue = 2
dp[0][0][1] = data[0][0]
dp[0][0][2] = data[0][0]
dp[0][1][0] = data[0][1]
dp[0][1][2] = data[0][1]
dp[0][2][0] = data[0][2]
dp[0][2][1] = data[0][2]

for i in range(1,N):
    dp[i][0][1] = min(dp[i-1][1][0],dp[i-1][1][2],dp[i-1][2][0],dp[i-1][2][1]) + data[i][0]
    dp[i][0][2] = min(dp[i-1][1][0],dp[i-1][1][2],dp[i-1][2][0],dp[i-1][2][1]) + data[i][0]
    dp[i][1][0] = min(dp[i-1][0][1],dp[i-1][0][2],dp[i-1][2][0],dp[i-1][2][1]) + data[i][1]
    dp[i][1][2] = min(dp[i-1][0][1],dp[i-1][0][2],dp[i-1][2][0],dp[i-1][2][1]) + data[i][1]
    dp[i][2][0] = min(dp[i-1][0][1],dp[i-1][0][2],dp[i-1][1][0],dp[i-1][1][2]) + data[i][2]
    dp[i][2][1] = min(dp[i-1][0][1],dp[i-1][0][2],dp[i-1][1][0],dp[i-1][1][2]) + data[i][2]

print(min(dp[N-1][0][1],dp[N-1][0][2],dp[N-1][1][0],dp[N-1][1][2],dp[N-1][2][0],dp[N-1][2][1]))
