import sys
sys.stdin = open("숫자만들기.txt")

def cal(num,cnt,idx):
    if num == 0: return cnt+data[idx+1]
    elif num == 1: return cnt-data[idx+1]
    elif num == 2: return cnt*data[idx+1]
    elif num == 3: return int(cnt/data[idx+1])

def DFS(idx,a,b,c,d,cnt):
    global myMax,myMin
    if a>op[0] or b>op[1] or c>op[2] or d>op[3]: return
    if a == op[0] and b == op[1] and c == op[2] and d == op[3]:
        if cnt>myMax:
            myMax = cnt
        if cnt<myMin:
            myMin =cnt
        return

    DFS(idx+1,a+1,b,c,d,cal(0,cnt,idx))
    DFS(idx+1,a,b+1,c,d,cal(1,cnt,idx))
    DFS(idx+1,a,b,c+1,d,cal(2,cnt,idx))
    DFS(idx+1,a,b,c,d+1,cal(3,cnt,idx))

for tc in range(int(input())):
    N = int(input())
    op = list(map(int,input().split()))
    data = list(map(int,input().split()))

    myMax = -987654321
    myMin = 987654321

    DFS(0,0,0,0,0,data[0])
    print("#{} {}".format(tc+1,myMax-myMin))
