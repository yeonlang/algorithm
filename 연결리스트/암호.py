import sys
sys.stdin = open("암호.txt","r")

class Node:
    def __init__(self,data,rlink=None,llink=None):
        self.data = data
        self.rlink = rlink
        self.llink = llink

def insert(start,end):
    value = start.data + end.data
    start.rlink = Node(value)
    start.rlink.llink = start
    start.rlink.rlink = end
    end.llink = start.rlink

for tc in range(int(input())):
    N,M,K = map(int,input().split())

    flag = True
    for i in map(int,input().split()):
        if flag:
            head = Node(i)
            last = head
            flag=False
            continue

        last.rlink = Node(i)
        last.rlink.llink = last
        last = last.rlink
    last.rlink = head
    head.llink = last

    now = head
    for i in range(K):
        for j in range(M):
            now=now.rlink
        pre=now.llink
        if pre == last:
            insert(pre,now)
            last=now.llink
        else:
            insert(pre,now)
        now=now.llink

    print("#{}".format(tc + 1), end=" ")
    count = 0
    for u in range(N+K):
        if count == 10:
            break
        print(last.data, end=" ")
        last = last.llink
        count+=1
    print()

    # 1 5 6 1 9 13 4 2 8 6
    # 2 1736 2514 778 169 667 498 329 715 386 958
    # 3 826 1494 668 954 375 1052 677 302 774 2234


