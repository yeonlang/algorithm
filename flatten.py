import sys
sys.stdin = open('flatten.txt', 'r')

for tc in range(1):
    N_start = 1
    N_end = 100
    dump = int(input())
    lst = list(map(int, input().split()))
    count = [ 0 for _ in range(N_end+1)]

    for count_plus in lst:
        count[count_plus]+=1

    for i in range(dump):
        for check in range(N_end,-1,-1):
            if count[check] == 0:
                continue

            count[check] -=1
            count[check-1] +=1
            if count[check] == 0:
                last = check-1
            else :
                last = check
            N_end = last
            break

        for check in range(N_start,N_end+1):
            if count[check] == 0:
                continue

            count[check] -=1
            count[check+1] +=1
            if count[check] == 0:
                start = check+1
            else :
                start = check

            N_start=start
            break

    result = last - start
    print(f"#{tc+1} {result}")