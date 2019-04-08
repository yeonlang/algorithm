import sys
sys.stdin = open("종이붙이기.txt")

def fill(sy,sx,val,num):
    for y in range(sy,sy+val):
        for x in range(sx,sx+val):
            data[y][x] = num

def read(sy,sx,val):
    for y in range(sy,sy+val):
        for x in range(sx,sx+val):
            if not data[y][x]:
                return False
    return True

def DFS(c,cnt,idx):
    global myMin
    if c>=myMin:
        return

    if cnt == findcnt:
        if c<myMin:
            myMin = c
        return

    for val in range(idx,0,-1):
        if op[val]:
            for y in range(N-val+1):
                for x in range(N-val+1):
                    if not visited[y*N+x][(y+val-1)*N+(x+val-1)] and read(y,x,val):
                        visited[y*N+x][(y+val-1)*N+(x+val-1)] = 1
                        op[val]-=1
                        fill(y,x,val,0)
                        DFS(c+1,cnt+val**2,val)
                        fill(y,x,val,1)
                        op[val]+=1

op = [0,5,5,5,5,5]
N = 10
data = [list(map(int,input().split())) for _ in range(N)]
myMin = 987654321
visited = [[0]*100 for _ in range(100)]
findcnt = 0
for y in range(N):
    for x in range(N):
        if data[y][x]:
            findcnt+=1

DFS(0,0,5)
if myMin == 987654321:
    print(-1)
else:
    print(myMin)