import sys
sys.stdin = open("2667.txt","r")

def Dfs(stack):
    count=1
    while stack:
        y,x=stack.pop()
        lst[y][x]=0
        for nxt in range(4):
            nxtY = y + dy[nxt]
            nxtX = x + dx[nxt]
            if 0<=nxtY<n and 0<=nxtX<n :
                if lst[nxtY][nxtX] != 0 :
                    count+=1
                    lst[nxtY][nxtX]=0
                    stack.append((nxtY,nxtX))

    return count

n=int(input())
lst=[]
for _ in range(n):
    lst.append(list(map(int,input())))

dx=[1,-1,0,0]
dy=[0,0,1,-1]
stack=[]
num=0
result=[]

for y in range(n):
    for x in range(n):
        if lst[y][x] != 0:
            num+=1
            result.append(Dfs([(y,x)]))

result.sort()
print(len(result))
for _ in range(len(result)):
    print(result[_])

