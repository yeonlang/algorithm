import sys
sys.stdin = open("LCD.txt")

def top(num):
    for i in num:
        if i == '1' or i == '4':
            print(" "*(s+2),end=" ")
        else:
            print(" "+("-"*s)+" ",end=" ")
    print()

def topmid(num):
    for i in num:
        #우측
        if i == '1' or i == '2' or i == '3' or i == '7':
            print(" "*(s+1)+"|",end=" ")
        #좌측
        elif i == '5' or i == '6':
            print("|"+" "*(s+1),end=" ")
        #우좌동시
        else:
            print("|"+(" "*s)+"|",end=" ")
    print()

def mid(num):
    for i in num:
        if i == '1' or i == '7' or i == '0':
            print(" "*(s+2),end=" ")
        else:
            print(" "+("-"*s)+" ",end=" ")
    print()

def bottommid(num):
    for i in num:
        # 우좌동시
        if i == '6' or i == '8' or i == '0':
            print("|"+(" "*s)+"|",end=" ")

        # 좌측
        elif i == '2':
            print("|"+" "*(s+1),end=" ")
        # 우측
        else:
            print(" "*(s+1)+"|",end=" ")
    print()

def bottom(num):
    for i in num:
        if i == '1' or i == '4' or i == '7':
            print(" "*(s+2),end=" ")
        else:
            print(" "+("-"*s)+" ",end=" ")
    print()


s, num = input().split()
s = int(s)
top(num)
for i in range(s):
    topmid(num)
mid(num)
for j in range(s):
    bottommid(num)
bottom(num)

