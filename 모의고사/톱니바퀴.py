import sys
sys.stdin = open("톱니바퀴.txt")
# 3, 7

class gear:
    def __init__(self,n1,n2,n3,n4,n5,n6,n7,n8,left,right):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6
        self.n7 = n7
        self.n8 = n8
        self.left = left
        self.right = right
        self.leftflag = False
        self.rightflag = False

    def turn(self,d):
        if d == 1:
            temp = self.n8
            self.n8 = self.n7
            self.n7 = self.n6
            self.n6 = self.n5
            self.n5 = self.n4
            self.n4 = self.n3
            self.n3 = self.n2
            self.n2 = self.n1
            self.n1 = temp
        if d == -1:
            temp = self.n1
            self.n1 = self.n2
            self.n2 = self.n3
            self.n3 = self.n4
            self.n4 = self.n5
            self.n5 = self.n6
            self.n6 = self.n7
            self.n7 = self.n8
            self.n8 = temp
        if self.left and self.leftflag:
            self.left.turnleft(-1 if d == 1 else 1)
        if self.right and self.rightflag:
            self.right.turnright(-1 if d == 1 else 1)

    def turnleft(self,d):
        if d == 1:
            temp = self.n8
            self.n8 = self.n7
            self.n7 = self.n6
            self.n6 = self.n5
            self.n5 = self.n4
            self.n4 = self.n3
            self.n3 = self.n2
            self.n2 = self.n1
            self.n1 = temp
        if d == -1:
            temp = self.n1
            self.n1 = self.n2
            self.n2 = self.n3
            self.n3 = self.n4
            self.n4 = self.n5
            self.n5 = self.n6
            self.n6 = self.n7
            self.n7 = self.n8
            self.n8 = temp
        if self.left and self.leftflag:
            self.left.turnleft(-1 if d == 1 else 1)

    def turnright(self,d):
        if d == 1:
            temp = self.n8
            self.n8 = self.n7
            self.n7 = self.n6
            self.n6 = self.n5
            self.n5 = self.n4
            self.n4 = self.n3
            self.n3 = self.n2
            self.n2 = self.n1
            self.n1 = temp
        if d == -1:
            temp = self.n1
            self.n1 = self.n2
            self.n2 = self.n3
            self.n3 = self.n4
            self.n4 = self.n5
            self.n5 = self.n6
            self.n6 = self.n7
            self.n7 = self.n8
            self.n8 = temp
        if self.right and self.rightflag:
            self.right.turnright(-1 if d == 1 else 1)

    def judge(self):
        if self.left and self.left.n3^self.n7:
            self.leftflag = True
        elif self.left:
            self.leftflag = False
        if self.right and self.right.n7^self.n3:
            self.rightflag = True
        elif self.right:
            self.rightflag = False

def judge():
    A.judge()
    B.judge()
    C.judge()
    D.judge()

g1,g2,g3,g4,g5,g6,g7,g8 = map(int,input())
A = gear(g1,g2,g3,g4,g5,g6,g7,g8,False,False)
g1,g2,g3,g4,g5,g6,g7,g8 = map(int,input())
B = gear(g1,g2,g3,g4,g5,g6,g7,g8,False,False)
g1,g2,g3,g4,g5,g6,g7,g8 = map(int,input())
C = gear(g1,g2,g3,g4,g5,g6,g7,g8,False,False)
g1,g2,g3,g4,g5,g6,g7,g8 = map(int,input())
D = gear(g1,g2,g3,g4,g5,g6,g7,g8,False,False)
A.right = B
B.left = A
B.right = C
C.left = B
C.right = D
D.left = C
judge()

result = 0
N = int(input())
for i in range(N):
    num,d = map(int,input().split())
    if num == 1: A.turn(d)
    elif num == 2: B.turn(d)
    elif num == 3: C.turn(d)
    elif num == 4: D.turn(d)
    judge()

if A.n1: result += 1
if B.n1: result += 2
if C.n1: result += 4
if D.n1: result += 8

print(result)


