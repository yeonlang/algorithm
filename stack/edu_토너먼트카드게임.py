import sys
sys.stdin = open("토너먼트.txt","r")

def winner(i,j):
    c=data[i] - data[j] + 3
    if c == 3 or c%3 == 1 :
        return i
    else :
        return j

def half(start,end):
    m=(end+start)//2
    if end-start == 0:
        return start
    elif end-start == 1:
        return winner(start,end)
    return winner(half(start,m),half(m+1,end))

for tc in range(int(input())):
    n=int(input())
    data = list(map(int,input().split()))
    print(f"#{tc+1} {half(0,n-1)+1}")



