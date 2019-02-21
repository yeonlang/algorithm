import sys
sys.stdin =open("4871.txt","r")

def DFS(start):
    visited[start] = 1
    for next in range(node+1):
        if my_map[start][next] and not visited[next]:
            DFS(next)

for tc in range(int(input())):
    node, edge = map(int,input().split())
    my_map = [[0]*(node+1) for _ in range(node+1)]
    visited = [0]*(node+1)

    for _ in range(edge):
        now, nxt = map(int,input().split())
        my_map[now][nxt] = 1

    start, willfind = map(int, input().split())
    DFS(start)
    print(f"#{tc+1} {visited[willfind]}")