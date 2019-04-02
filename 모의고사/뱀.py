import sys
sys.stdin = open("뱀.txt")

def end(y,x): return True if not 0<=y<N or not 0<=x<N or data[y][x] == 2 else False
def search(hy,hx,ry,rx,d):
    time = 0
    data[ry][rx] = 2
    r = 0
    dr = 0
    while True:
        if d+direct[time]>3 :
            d = 0
        elif d+direct[time]<0 :
            d = 3
        else:
            d = d+direct[time]
        hy+=dy[d]
        hx+=dx[d]
        if end(hy,hx):
            return time+1
        if not data[hy][hx] :
            data[ry][rx] = 0
            if dr+direct[r]>3:
                dr = 0
            elif dr+direct[r]<0:
                dr = 3
            else:
                dr = dr+direct[r]
            ry+=dy[dr]
            rx+=dx[dr]
            r+=1
        data[hy][hx] = 2
        time+=1

# 우 하 좌 상
dy = [0,1,0,-1]
dx = [1,0,-1,0]

N = int(input())
K = int(input())
data = [[0]*N for _ in range(N)]
for _ in range(K):
    y, x = map(lambda x:int(x)-1,input().split())
    data[y][x] = 1

direct = [0]*10001

L = int(input())
for _ in range(L):
    t, d = input().split()
    t = int(t)
    if d == 'D':
        d = 1
    elif d == 'L':
        d = -1
    direct[t] = d

print(search(0,0,0,0,0))









