class Node:
    def __init__(self,data,link = None):
        self.data = data
        self.link = link

def dead():
    global head
    if head.link.link == head:
        print(head.data)
        print(head.link.data)
        return False
    else:
        temp = head
        head = temp.link.link.link
        temp.link.link = head
        return True

def Enqueue(item):
    global head
    newNode = Node(item)
    if head == None: head = newNode
    else:
        pre = head
        nxt = pre.link
        while nxt and nxt.data<item:
            pre = nxt
            nxt=nxt.link
        newNode.link = nxt
        pre.link = newNode


head = None
for i in range(1,42):
    Enqueue(i)

p = head
while p.link != None:
    p = p.link
p.link = head

while dead(): pass