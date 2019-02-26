import sys
sys.stdin=open("edu_연습문제3.txt","r")

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
    global count
    enque(start)

    while front != rear:
        now=deque()
        print(f"{now} 는 거리가 {visited[now]-1}입니다")
        for nxt in range(v+1):
            if matrix[now][nxt] and not visited[nxt] :
                visited[nxt] = visited[now]+1
                enque(nxt)

que = [0]*50
front = -1
rear = -1
count = 0

data = list(map(int, input().split()))
v = max(data)
matrix = [ [0]*(v+1) for _ in range(v+1)]
visited = [0]*(v+1)

for i in range(len(data)//2):
    now=data[2*i]
    nxt=data[2*i+1]
    matrix[now][nxt] = 1
    matrix[nxt][now] = 1

visited[1] = 1
bfs(1)



