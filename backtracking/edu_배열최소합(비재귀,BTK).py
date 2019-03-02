import sys
sys.stdin = open("배열최소합.txt","r")

def getsum(start):
    global minsum
    stack = [start]
    while stack:
        y, nowsum, visited = stack.pop()
        if y >= n:
            if nowsum < minsum:
                minsum = nowsum
            continue

        if nowsum > minsum:
            continue

        for x in range(n):
            if x not in visited :
                nowsum += data[y][x]
                visited.append(x)
                stack.append((y+1,nowsum,visited[:]))
                visited.pop()
                nowsum -= data[y][x]



for tc in range(int(input())):
    n=int(input())
    data=[]
    for i in range(n):
        data.append(list(map(int,input().split())))

    minsum = 10*n

    getsum((0,0,[]))
    print(f"#{tc + 1} {minsum}")
