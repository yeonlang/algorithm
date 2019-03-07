import sys
sys.stdin = open('prefix_sum.txt', 'r') #파일에서 읽을때 사용

for tc in range(int(input())):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))

    my_min = 10000*M
    my_max = 0

    for index in range(M-1,N):
        m=M
        count = 0
        while m>0:
            count+=lst[index-m+1]
            m-=1

        if count>my_max:
            my_max=count
        if count<my_min:
            my_min=count

    print(f"#{tc+1} {my_max-my_min}")



