import sys
sys.stdin = open("미로.txt","r")

def dfs(start):
    global result,data
    y, x = start
    if data[y][x] == 3:
        result=1
    data[y][x] = 1
    for i in range(4):
        ny=y+dy[i]
        nx=x+dx[i]
        if 0<=ny<n and 0<=nx<n and data[ny][nx] != 1:
            dfs((ny,nx))



dx=[1,0,-1,0]
dy=[0,1,0,-1]

for tc in range(int(input())):
    n=int(input())
    data=[]

    result = 0

    for y in range(n):
        lst=list(map(int,input()))
        if 2 in lst:
            start=(y,lst.index(2))
        data.append(lst)
        del lst

    dfs(start)
    print(f'#{tc+1} {result}')


