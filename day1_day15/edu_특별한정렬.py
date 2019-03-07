import sys
sys.stdin = open("sw4843.txt","r")

def mysort(lst,num):
    if num&1:
        return lst.pop(lst.index(min(lst)))
    else :
        return lst.pop(lst.index(max(lst)))

for tc in range(int(input())):
    n=int(input())
    lst=list(map(int, input().split()))
    result=[]

    for i in range(10):
        result.append(mysort(lst,i))

    print(f"#{tc+1}",*result)