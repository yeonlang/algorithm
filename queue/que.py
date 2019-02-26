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

que = [0]*20
front = -1
rear = -1



