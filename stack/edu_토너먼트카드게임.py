import sys
sys.stdin = open("토너먼트.txt","r")

def winner(a,b):
    if a[0][1] == b[0][1]:
        return a
    if a[0][1] == 3 or b[0][1] == 3:
        if a[0][1] == 1:
            return a
        if b[0][1] == 1:
            return b

    if a[0][1] > b[0][1]:
        return a
    else:
        return b

def half(data):
    length = len(data)
    if length == 1:
        return data
    if length == 2:
        return winner(data[:1],data[1:])

    return winner(half(data[:length//2]),half(data[length//2:]))


for tc in range(int(input())):
    n=int(input())
    data = list( (i+1,j) for i,j in enumerate(map(int,input().split())))
    print(f"#{tc+1} {half(data)[0][0]}")



