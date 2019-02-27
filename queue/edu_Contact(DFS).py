import sys
sys.stdin = open("Contact.txt","r")

def dfs(start):
    stack=[start]

    while stack :
        now = stack.pop()
        for nxt in range(v):
            if data[now][nxt] and (not visited[nxt] or visited[now]+1<visited[nxt]):
                visited[nxt] = visited[now] + 1
                stack.append(nxt)

for tc in range(10):
    n, start = map(int,input().split())
    info = list(map(int, input().split()))
    v = max(info)
    data=[[0]*(v+1) for _ in range(v+1)]
    visited=[0]*(v+1)

    for i in range(len(info)//2):
        now = info[2*i]
        nxt = info[2*i+1]
        data[now][nxt] = 1

    visited[start]=1
    dfs(start)

    M=max(visited)
    result=0
    for i in range(v+1):
        if visited[i] == M and i>result:


    print(f"#{tc+1} {result}")
