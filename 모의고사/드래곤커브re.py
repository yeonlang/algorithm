import sys
sys.stdin = open("드래곤커브.txt")

def read(sy,sx):
    data[sy][sx] = 1
    for i in direct:
        sy+=dy[i]
        sx+=dx[i]
        data[sy][sx] = 1

#우상좌하
dy = [0,-1,0,1]
dx = [1,0,-1,0]
data = [[0]*101 for _ in range(101)]
N = int(input())
for y in range(N):
    sx, sy, d, g =map(int,input().split())

    direct = [d]
    while g:
        l = len(direct)
        for i in range(l-1,-1,-1):
            direct.append(0 if direct[i] == 3 else direct[i]+1)
        g-=1
    read(sy,sx)

cnt = 0
for y in range(100):
    for x in range(100):
        if data[y][x] and data[y+1][x] and data[y][x+1] and data[y+1][x+1]:
            cnt+=1
print(cnt)
