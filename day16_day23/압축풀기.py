for tc in range(int(input())):
    N = int(input())
    result = []
    for i in range(N):
        alpa, num = input().split()
        num = int(num)
        result+=list(alpa)*num
    print("#{}".format(tc+1))
    t = 1
    while t<=len(result):
        print(result[t-1],end="")
        if t%10 == 0:
            print()
        t+=1
    print()

