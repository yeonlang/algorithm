class Node:
    def __init__(self,data,link = None):
        self.data = data
        self.link = link

def Enqueue(item):
    global head
    newNode = Node(item)
    if head == None: head = newNode
    else:
        p = head
        while p.link :
            p=p.link
        p.link=newNode

head = None
Enqueue(1)
Enqueue(5)
Enqueue(2)
Enqueue(4)
Enqueue(3)

p = head
while p != None:
    print(p.data)
    p = p.link
