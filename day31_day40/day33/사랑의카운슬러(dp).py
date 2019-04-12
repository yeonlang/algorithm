import sys
sys.stdin = open("사랑의카운슬러.txt")

def DFS(c,x):
    global myMin
    if dp[x]: return 1
    if c==N//2:
        y,x = 0,0
        for i in left:
            y+=data[i][0]
            x+=data[i][1]
        for j in right:
            y-=data[j][0]
            x-=data[j][1]
        temp = y**2+x**2
        if temp<myMin or myMin == -1:
            myMin = temp
        return 1
    for i in range(N):
        for j in range(N):
            if not visited[i] and not visited[j] and i!=j:
                visited[i] = 1
                visited[j] = 1
                left.append(i)
                right.append(j)
                dp[x] += DFS(c+1,x+(1<<i)+(1<<(j+1)))
                left.pop()
                right.pop()
                visited[i] = 0
                visited[j] = 0
    return 1

for tc in range(int(input())):
    N = int(input())
    data = []
    for _ in range(N):
        y,x = map(int,input().split())
        data.append((y,x))
    result = []
    dp = [0]*(1<<N+1)
    myMin = -1
    visited = [0]*N
    left =[]
    right =[]
    DFS(0,0)
    print("#{} {}".format(tc+1,myMin))