import sys
sys.stdin = open("가능한시험점수.txt","r")

for tc in range(int(input())):
    N = int(input())
    data = list(map(int,input().split()))
    result = set()
    for i in range(1<<N):
        num = 0
        for j in range(N):
            if i & (1 << j):
                num+=data[j]
        result.add(num)

    print("#{} {}".format(tc+1,len(result)))