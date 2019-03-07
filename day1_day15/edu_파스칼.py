import sys
sys.stdin = open("파스칼.txt","r")

def func(y,x):
    result = 0
    if 0<=x<y:
        result+=data[y-1][x]
    if 0<=x-1<y:
        result+=data[y-1][x-1]
    return result

for tc in range(int(input())):
    n = int(input())
    data = [[1]]
    for y in range(1,n):
        data.append([])
        for x in range(len(data[y-1])+1):
            data[y].append(func(y,x))
    print("#{}".format(tc+1))
    for ans in data:
        print(*ans)



