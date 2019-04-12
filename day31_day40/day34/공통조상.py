import sys
sys.stdin = open("공통조상.txt")

class tree:
    def __init__(self,ID):
        self.id = ID
        self.left_child = False
        self.right_child = False
        self.level = 0
    def findlevel(self,level):
        self.level = level+1
        if self.left_child:
            self.left_child.findlevel(self.level)
        if self.right_child:
            self.right_child.findlevel(self.level)
    def findsubtree(self):
        if not self.left_child and not self.right_child: return 1
        cnt = 0
        if self.left_child:
            cnt += self.left_child.findsubtree()
        if self.right_child:
            cnt += self.right_child.findsubtree()
        return cnt+1

for tc in range(int(input())):
    V,E, a,b = map(int,input().split())
    data = [0]*(V+1)
    for i in range(1,V+1):
        data[i] = tree(i)
    In = list(map(int,input().split()))
    for i in range(E):
        if not data[In[i*2]].left_child:
            data[In[i*2]].left_child = data[In[i*2+1]]
        else :
            data[In[i*2]].right_child = data[In[i*2+1]]
        data[In[i*2+1]].parent = data[In[i*2]]

    data[1].findlevel(0)
    A = data[a]
    B = data[b]
    while A.level != B.level or A.level == 1 or B.level == 1:
        if A.level>B.level:
            A = A.parent
        else:
            B = B.parent

    while A != B:
        A = A.parent
        B = B.parent

    result = A.findsubtree()
    print("#{} {} {}".format(tc+1, A.id, result))

    # 1 3 8
    # 2 1 10
    # 3 21 35
    # 4 1 100
    # 5 168 107
    # 6 1 500
    # 7 398 840
    # 8 747 1359
    # 9 498 3141
    # 10 7165 2435













