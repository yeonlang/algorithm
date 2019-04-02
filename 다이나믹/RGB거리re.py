import sys
sys.stdin = open("RGB거리.txt")

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]

D = [[0]*3 for _ in range(N)]
D[0][0] = data[0][0]
D[0][1] = data[0][1]
D[0][2] = data[0][2]

for k in range(1,N):
    D[k][0] = min(D[k-1][1],D[k-1][2]) + data[k][0]
    D[k][1] = min(D[k-1][0],D[k-1][2]) + data[k][1]
    D[k][2] = min(D[k-1][0],D[k-1][1]) + data[k][2]
print(min(D[k][0],D[k][1],D[k][2]))

