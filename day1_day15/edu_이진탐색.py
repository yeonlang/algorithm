import sys
sys.stdin = open("sw4839.txt","r")

def search(r,p):
    l=1
    count=0

    while True:
        count+=1
        c = int((l + r) / 2)
        if c==p:
            return count
        elif c>p:
            r=c
        else :
            l=c


for tc in range(int(input())):
    l=1
    r, Pa, Pb = map(int, input().split())
    a=search(r,Pa)
    b=search(r,Pb)

    if a>b:
        result='B'
    elif a<b:
        result='A'
    else:
        result=0

    print(f"#{tc+1} {result}")
