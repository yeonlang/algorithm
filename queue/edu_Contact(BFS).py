import sys
sys.stdin = open("Contact.txt","r")

def enque(item):
    global que, rear
    rear += 1
    que[rear]=item

def deque():
    global front
    front += 1
    temp = que[front]
    que[front] = 0
    return temp

def bfs(start):
    enque(start)

    while rear != front :
        now = deque()
        for nxt in range(v):
            if data[now][nxt] and not visited[nxt]:
                visited[nxt] = visited[now] + 1
                enque(nxt)


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

    que = [0] * 10000
    front = -1
    rear = -1

    visited[start]=1
    bfs(start)

    M=max(visited)
    result=0
    for i in range(v+1):
        if visited[i] == M and i>result:
            result = i
    print(f"#{tc+1} {result}")

