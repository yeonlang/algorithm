import sys
sys.stdin = open("리모콘.txt","r")

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
    enque(start)

    while rear != front:
        now = deque()
        for i in range(6):
            nxt = now + delta[i]
            if 0<=nxt+10<n+20 and not visited[nxt+10]:
                visited[nxt+10] = visited[now+10]+[delta[i]]
                if nxt == there:
                    return visited[nxt+10]
                enque(nxt)
    return 0
for i in range(13):
    go, there = map(int,input().split())
    delta = [10, -10, 5, -5, 1, -1]
    n=max(go,there)
    visited = [0]*(n+21)

    que=[0]*10000
    front=-1
    rear=-1

    visited[go+10]=[]

    print(f"{go}에서 {there}까지 가장 적은 버튼 조작횟수는 ?")
    print(bfs(go))