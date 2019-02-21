import sys
sys.stdin =open("input3.txt","r")

MyMap = [[0]*8 for i in range(8)]
visited=[0]*8
stack=[0]*10000
top=-1

def push(x):
    global stack, top
    top += 1
    stack[top]=x

def pop():
    global stack, top
    if top == -1:
        return
    top -= 1
    return stack[top+1]

def findnext(here):
    for next in range(8):
        if MyMap[here][next] and not visited[next]:
            return next

def DFS(here):
    global top
    print(here)
    visited[here] = True

    while here:
        next = findnext(here)
        while next:
            here = next
            print(here)
            visited[here] = True
            next = findnext(here)
            push(here)
        here = pop()

Data = list(map(int,input().split()))
n=len(Data)//2
for i in range(n):
    start= Data[i*2]
    stop = Data[i*2-1]
    MyMap[start][stop] = 1
    MyMap[stop][start] = 1

DFS(1)

