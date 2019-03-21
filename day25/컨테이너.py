import sys
sys.stdin = open("컨테이너.txt")


for tc in range(int(input())):
    N,M = map(int,input().split())
    container = list(map(int,input().split()))
    truck = list(map(int,input().split()))
    container.sort(reverse=True)
    truck.sort(reverse=True)

    i = 0
    j = 0
    result = 0
    while j != M and i != N:
        if truck[j] >= container[i]:
            result+=container[i]
            j,i= j+1,i+1
            continue
        if truck[j] < container[i]:
            i+=1

    print("#{} {}".format(tc+1,result))
