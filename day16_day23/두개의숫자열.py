import sys
sys.stdin = open("두개의숫자열.txt","r")

for tc in range(int(input())):
    L,S = map(int,input().split())
    l_data = list(map(int,input().split()))
    s_data = list(map(int,input().split()))

    if L<S:
        L,S = S,L
    if len(l_data) < len(s_data):
        l_data,s_data = s_data[:],l_data[:]

    my_max = 0
    for i in range(L-S+1):
        result = 0
        for j in range(S):
            result+=l_data[j+i]*s_data[j]
        if result>my_max:
            my_max = result
    print("#{} {}".format(tc+1,my_max))

    # 1 30
    # 2 63
    # 3 140
    # 4 181
    # 5 63
    # 6 58
    # 7 22
    # 8 120
    # 9 96
    # 10 70
