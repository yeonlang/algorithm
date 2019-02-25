import sys
sys.stdin = open("자성체.txt","r")

def bt(start):
    global ans
    lst=[]
    for i in range(n):
        lst.append(data[i][start])
    result=[]
    for i in range(n):
        if lst[i] == 1:
            result.append((i,1))
        if lst[i] == 2:
            result.append((i,2))
    for j in range(len(result)-1):
        if result[j][1] == 1 and result[j+1][1] == 2 :
            ans+=1


for tc in range(10):
    ans=0
    n=int(input())
    data=[ list(map(int,input().split())) for _ in range(n) ]
    for i in range(n):
        bt(i)
    print(f"#{tc+1} {ans}")
