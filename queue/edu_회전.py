import sys
sys.stdin = open("회전.txt","r")

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

for tc in range(int(input())):
    n,m = map(int,input().split())

    que = [0] * 10000
    front = -1
    rear = -1

    for i in map(int,input().split()):
        enque(i)

    for i in range(m):
        shift()

    print(f"#{tc+1} {que[front+1]}")