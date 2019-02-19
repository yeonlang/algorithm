import sys
sys.stdin = open('min_max.txt', 'r') #파일에서 읽을때 사용

for tc in range(int(input())):
    N=int(input())
    lst = list(map(int,input().split()))
    count = [0]*(10**6+1)
    result = []
    for count_plus in lst:
        count[count_plus] +=1

    for count_min in range(1,10**6+1):
        if count[count_min] == 0:
            continue
        else:
            result.append(count_min)
            break

    for count_max in range(10**6,-1,-1):
        if count[count_max] == 0:
            continue
        else:
            result.append(count_max)
            break

    print(f"#{tc+1} {result[1]-result[0]}")