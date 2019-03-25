import sys
sys.stdin = open("연산자끼워넣기.txt")

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


N = int(input())
visited = [0]*(N-1)
data = list(map(int,input().split()))
operator = list(map(int,input().split()))

myMax = -1187654321
myMin = 1187654321
BTK(0,N,data[0])

print(myMax)
print(myMin)