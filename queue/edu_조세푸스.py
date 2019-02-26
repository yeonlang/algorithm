def enque(item):
    global rear,que
    rear = (rear + 1)%len(que)
    que[rear]=item


def deque():
    global front,que
    count = 0
    for i in range(1,41*3+1):
        if que[(front+i)%41] != 0:
            count+=1
        if count == 3:
            front=(front+i)%41
            que[front] = 0
            break

    que[front] = 0

que=[0]*41
front = 0
rear = 0

n=41
for i in range(1,n+1):
    enque(i)

for j in range(39):
    deque()

print(que)
print(front,rear)