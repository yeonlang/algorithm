import sys
sys.stdin = open("숫자만들기.txt")

def cal(num,cnt,choice):
    if num == 0: return cnt+data[choice+1]
    elif num == 1: return cnt-data[choice+1]
    elif num == 2: return cnt*data[choice+1]
    elif num == 3: return int(cnt/data[choice+1])

def BTK(choice,N,cnt):
    global myMax , myMin
    if choice == N-1:
        if cnt>=myMax:
            myMax = cnt
        if cnt<=myMin:
            myMin = cnt
        return

    for i in range(4):
        if operator[i]>0:
            operator[i] -= 1
            BTK(choice+1,N,cal(i,cnt,choice))
            operator[i] += 1

for tc in range(int(input())):
    N = int(input())
    visited = [0]*(N-1)
    operator = list(map(int,input().split()))
    data = list(map(int,input().split()))

    myMax = -987654321
    myMin = 987654321
    BTK(0,N,data[0])

    print("#{} {}".format(tc+1,myMax-myMin))

    # 1 24
    # 2 8
    # 3 144
    # 4 8
    # 5 91
    # 6 150
    # 7 198
    # 8 2160
    # 9 46652
    # 10 701696
