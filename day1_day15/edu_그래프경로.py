import sys
sys.stdin =open("4871.txt","r")

def deque():
    global front
    front+=1
    temp = que[front]
    que[front]=0
    return temp

def enque(item):
    global rear
    rear+=1
    que[rear]=item

def bfs(start):
    global result,data
    enque(start)

    while rear != front:
        y,x = deque()
        for i in range(4):
            ny=y+dy[i]
            nx=x+dx[i]
            if 0<=ny<n and 0<=nx<n and data[ny][nx] != 1:
                if data[ny][nx] == 3:
                    return 1
                data[ny][nx] = 1
                enque((ny,nx))
    return 0

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