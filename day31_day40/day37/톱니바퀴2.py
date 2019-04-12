import sys
sys.stdin = open("톱니바퀴2.txt")

class gear:
    def __init__(self,n1,n2,n3,n4,n5,n6,n7,n8):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.n7 = n7
        self.n8 = n8
        self.left = False
        self.leftflag= False
        self.right = False
        self.rightflag= False

    def turn(self,d):
        #시계방향
        if d == 1:
            t = self.n4
            self.n1,self.n2,self.n3,self.n4 = self.n8,self.n1,self.n2,self.n3
            self.n5,self.n6,self.n7,self.n8 = t, self.n5,self.n6,self.n7

        #반시계방향
        if d == -1:
            t = self.n1
            self.n1,self.n2,self.n3,self.n4 = self.n2,self.n3,self.n4,self.n5
            self.n5,self.n6,self.n7,self.n8 = self.n6,self.n7,self.n8,t

        if self.right and self.rightflag:
            self.right.Rturn(-d)
        if self.left and self.leftflag:
            self.left.Lturn(-d)



    def Rturn(self,d):
        # 시계방향
        if d == 1:
            t = self.n4
            self.n1,self.n2,self.n3,self.n4 = self.n8,self.n1,self.n2,self.n3
            self.n5,self.n6,self.n7,self.n8 = t,self.n5,self.n6,self.n7

        # 반시계방향
        if d == -1:
            t = self.n1
            self.n1,self.n2,self.n3,self.n4 = self.n2,self.n3,self.n4,self.n5
            self.n5,self.n6,self.n7,self.n8 = self.n6,self.n7,self.n8,t

        if self.right and self.rightflag:
            self.right.Rturn(-d)

    def Lturn(self,d):
        # 시계방향
        if d == 1:
            t = self.n4
            self.n1,self.n2,self.n3,self.n4 = self.n8,self.n1,self.n2,self.n3
            self.n5,self.n6,self.n7,self.n8 = t,self.n5,self.n6,self.n7

        # 반시계방향
        if d == -1:
            t = self.n1
            self.n1,self.n2,self.n3,self.n4 = self.n2,self.n3,self.n4,self.n5
            self.n5,self.n6,self.n7,self.n8 = self.n6,self.n7,self.n8,t

        if self.left and self.leftflag:
            self.left.Lturn(-d)

def array():
    for i in range(N):
        if data[i].left:
            if data[i].n7 == data[i-1].n3:
                data[i].leftflag = False
            else:
                data[i].leftflag = True
        if data[i].right:
            if data[i].n3 == data[i+1].n7:
                data[i].rightflag = False
            else:
                data[i].rightflag = True

N = int(input())
data = [0]*N
for i in range(N):
    n1,n2,n3,n4,n5,n6,n7,n8 = map(int,input())
    data[i] = gear(n1,n2,n3,n4,n5,n6,n7,n8)
    if 1<=i:
        data[i].left = data[i-1]
        data[i-1].right = data[i]
array()
K = int(input())
for j in range(K):
    c, d = map(int,input().split())
    data[c-1].turn(d)
    array()

cnt = 0
for k in data:
    if k.n1:
        cnt+=1
print(cnt)
