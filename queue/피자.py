import sys
sys.stdin = open("피자.txt","r")

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

def shift():
    enque(deque())

def fire():
    global count

    while que.count(0) != len(que)-1:
        if que[rear-n+1] != 0:
            if data[que[rear-n+1]] != 0:
                data[que[rear-n+1]]=data[que[rear-n+1]]//2
            if data[que[rear-n+1]] == 0:
                deque()
        if que[rear-n+1] == 0:
            count += 1
            if count <= m:
                enque(count)
            elif rear-front < n:
                enque(0)
        shift()

for tc in range(int(input())):
    n,m = map(int,input().split())
    data =[0]+list(map(int,input().split()))
    count=n

    que = [0]*10000
    front = -1
    rear = -1

    for i in range(1,n+1):
        enque(i)

    fire()
    print(f"#{tc+1} {max(que)}")



