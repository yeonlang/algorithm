import sys
sys.stdin = open("숫자추가.txt","r")

class Node:
    def __init__(self,data,link=None):
        self.data = data
        self.link = link

def insert(num,value):
    t = 1
    pre = head
    while t<num:
        pre=pre.link
        t+=1
    nxt=pre.link
    pre.link = Node(value)
    pre.link.link = nxt

for tc in range(int(input())):
    N,M,L = map(int,input().split())

    flag = True
    for i in map(int,input().split()):
        if flag:
            head = Node(i)
            p = head
            flag=False
            continue

        p.link = Node(i)
        p=p.link
    for j in range(M):
        num, value = map(int,input().split())
        insert(num,value)

    t=0
    pre = head
    while t<L:
        pre = pre.link
        t+=1
    print("#{} {}".format(tc+1,pre.data))





