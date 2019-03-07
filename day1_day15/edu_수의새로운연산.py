import sys
sys.stdin = open("새로운연산.txt","r")

def func1(num):
    n = 0
    while True:
        if (n*(n+1))//2<num<=((n+1)*(n+2))//2 :
            return ((n+1)-(num-(n*(n+1))//2)+1,num-(n*(n+1))//2)
        n+=1

def func2(y,x):
    num = x+y-1
    return (num**2-num+2)//2+x-1

for tc in range(int(input())):
    a, b = map(int,input().split())
    Py,Px = func1(a)
    Qy,Qx = func1(b)
    ny,nx = Py+Qy,Px+Qx
    result = func2(ny,nx)
    print("#{} {}".format(tc+1,result))

