
N = int(input())
data = [ list(map(int,input().split())) for _ in range(N) ]
for y in range(N):
    for x in range(N):
        data