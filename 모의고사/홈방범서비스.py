import sys
sys.stdin = open("홈방범서비스.txt","r")

from collections import deque

def bfs(y,x,K,count):
    global revenue
    que = deque()
    append = que.append
    pop = que.popleft

    append((y,x))
    while que:
        y,x = pop()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0<=ny<n and 0<=nx<n and not visited[ny][nx] :
                temp = visited[y][x] + 1
                if temp <= K:
                    append((ny,nx))
                    visited[ny][nx] = temp
                    if data[ny][nx] :
                        count+=revenue
    return count

def solution():
    global revenue,result,visited

    for K in range(2*n-1,0,-1):
        cost = K**2+(K-1)**2
        if result>cost:
            return
        for y in range(n):
            for x in range(n):
                visited = [[0] * n for _ in range(n)]
                count = 0
                visited[y][x] = 1
                if data[y][x]:
                    count+=revenue
                temp2 = bfs(y,x,K,count)
                if temp2-cost>=0 and temp2//revenue > result:
                    result=temp2//revenue

for tc in range(int(input())):
    #크기 n, 수익 revenue
    n,revenue = map(int,input().split())
    result = 0
    dy = [0,0,1,-1]
    dx = [1,-1,0,0]

    data = [ list(map(int,input().split())) for _ in range(n)]

    solution()
    print("#{} {}".format(tc+1,result))





