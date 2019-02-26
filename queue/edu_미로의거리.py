import sys
sys.stdin=open("미로의거리.txt","r")

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
            if 0<=ny<n and 0<=nx<n and data[ny][nx] == 3:
                return data[y][x]-2
            if 0<=ny<n and 0<=nx<n and data[ny][nx] == 0:
                data[ny][nx] = data[y][x]+2
                enque((ny,nx))
    return 0
for tc in range(int(input())):
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    que=[0]*10000
    front=-1
    rear=-1

    n=int(input())
    data=[]

    result = False

    for y in range(n):
        lst=list(map(int,input()))
        if 2 in lst:
            start=(y,lst.index(2))
        data.append(lst)
        del lst


    print(f'#{tc+1} {bfs(start)//2}')