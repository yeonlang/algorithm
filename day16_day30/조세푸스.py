class Node:
    def __init__(self,data,link = None):
        self.data = data
        self.link = link

def Enqueue(item):
    global head
    newNode = Node(item)
    if head == None: head = newNode
    else:
        pre = head
        p = pre.link
        while p and p.data<item:
            pre = p
            p=p.link
        newNode.link = p
        pre.link = newNode


head = None
Enqueue(1)
Enqueue(5)
Enqueue(2)
Enqueue(4)
Enqueue(3)


p = head
while p!=None:
    print(p.data)
    p = p.link
p = head