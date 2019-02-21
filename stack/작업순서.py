import sys
sys.stdin = open("작업순서.txt","r")

def dfs(start):
    stack=[start]
    while stack:
        now = stack.pop()
        visited[now] +=1
        print(now, end=" ")

        for nxt in range(1,node+1):
            if data[now][nxt] and isPossible(nxt) :
                stack.append(nxt)


def isPossible(now):
    for i in range(node+1):
        if reverse_data[now][i]==1:
            if visited[i] == 0:
                return False
    return True

for tc in range(10):
    print(f'#{tc+1}',end=" ")
    node, edge = map(int,input().split())
    edge_data = list(map(int, input().split()))
    n = len(edge_data) // 2

    data = [ [0]*(node+1) for i in range(node+1)]
    reverse_data = [ [0]*(node+1) for i in range(node+1)]
    visited = [0]*(node+1)

    for i in range(n):
        start = edge_data[i * 2]
        stop = edge_data[i * 2 - 1]
        data[start][stop] = 1
        reverse_data[stop][start] =1

    for j in range(1,node+1):
        if isPossible(j) and not visited[j]:
            dfs(j)
    print()