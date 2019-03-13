import sys
sys.stdin = open("수열추가.txt","r")

class Node:
    def __init__(self,data,rlink=None,llink=None):
        self.data = data
        self.rlink = rlink
        self.llink = llink

def insert(start,end,rear,tail):
    global last,head
    if start:
        start.rlink = rear
        rear.llink = start
    else:
        head = rear

    if end:
        end.llink = tail
        tail.rlink = end
    else:
        last=tail

for tc in range(int(input())):
    N,M= map(int,input().split())

    flag = True
    for i in map(int,input().split()):
        if flag:
            head = Node(i)
            p = head
            flag=False
            continue

        p.rlink = Node(i)
        p.rlink.llink = p
        p=p.rlink

    last = p
    for j in range(1,M):
        flag = True
        for k in map(int, input().split()):
            if flag:
                newhead = Node(k)

                temp = head
                if temp.data>k:
                    end=temp
                    start=None
                else:
                    while True:
                        temp = temp.rlink
                        if temp.data>k:
                            end = temp
                            start = temp.llink
                            break
                        elif not temp.rlink:
                            start=temp
                            end = None
                            break

                np = newhead
                flag = False
                continue

            np.rlink = Node(k)
            np.rlink.llink = np

            np = np.rlink

        insert(start,end,newhead,np)

    print("#{}".format(tc+1),end=" ")
    for u in range(10):
        print(last.data,end=" ")
        last=last.llink
    print()








