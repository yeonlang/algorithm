import sys
sys.stdin = open("웜바이러스.txt")

N = int(input())
M = int(input())
myMap = [[0]*N for _ in range(N)]

for i in range(M):
    a,b = map(int,input().split())
    myMap[a-1][b-1] = 1
    myMap[b-1][a-1] = 1

for k in range(N):
    for start in range(N):
        for end in range(N):
            myMap[start][end] = myMap[start][end]|(myMap[start][k]&myMap[k][end])

cnt = -1
for j in range(N):
    if myMap[0][j] == 1: cnt+=1
print(cnt)