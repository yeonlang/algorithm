class link:
    def __init__(self,val,i):
        self.val = val
        self.id = i
        self.flag = True if i == 1 else False

def cut(i):
    cnt = que[i].left.val*que[i].right.val
    que[i].left.right = que[i].right
    que[i].right.left = que[i].left
    return cnt

def back(i):
    que[i].left.right = que[i]
    que[i].right.left = que[i]

def DFS(c,cnt):
    global myMax
    if c == N-2:
        if cnt>myMax:
            myMax = cnt
        return

    for i in range(1,N-1):
        if que[i]:
            tp = que[i]
            a = cut(i)
            que[i] = 0
            DFS(c+1,cnt+a)
            que[i] = tp
            back(i)

N = int(input())
i = 1
que = [0]*N
for val in map(int,input().split()):
    que[i-1] = link(val,i)
    if que[i-1].flag:
        i+=1
        continue
    que[i-1].left = que[i-2]
    que[i-2].right = que[i-1]
    i+=1
myMax = 0
DFS(0,0)
print(myMax)
