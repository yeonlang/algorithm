def enque(item):
    global rear
    que[rear]=item
    rear = (rear+1)%20


def deque():
    global front
    front = (front+1)%20
    que[front] = 0

que=[0]*20
rear = 0
front = 0
