import sys
sys.stdin = open("이진탐색.txt")

for tc in range(int(input())):
    N,M = map(int,input().split())
    data = list(map(int,input().split()))
    value = list(map(int,input().split()))
    cnt = 0
    data.sort()
    for i in range(M):
        find = value[i]
        start = 0
        end = N-1
        flag = 3
        while True:
            mid = (start+end)//2
            if find == data[mid]:
                break
            elif find > data[mid] :
                if flag == 1 or flag == 3:
                    flag = 2
                else:
                    flag = 0
                    break
                start = mid + 1
            elif find < data[mid]:
                if flag == 2 or flag == 3:
                    flag = 1
                else:
                    flag = 0
                    break
                end = mid - 1

        if flag:
            cnt+=1

    print("#{} {}".format(tc+1,cnt))

#1 2
#2 0
#3 3
#4 1
#5 1
#6 5
#7 4
#8 20
#9 29
#10 29

