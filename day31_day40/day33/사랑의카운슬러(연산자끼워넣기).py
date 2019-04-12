import sys
sys.stdin = open("사랑의카운슬러.txt")

def DFS(c, sumX, sumY):
    global myMin
    if c == N:
        temp = sumX**2+sumY**2
        if temp<myMin or myMin == -1:
            myMin = temp
        return
    if not myMin: return
    for i in range(2):
        if op[i]:
            op[i]-=1
            if i:
                DFS(c+1,sumX+data[c][0], sumY+data[c][1])
            else:
                DFS(c+1,sumX-data[c][0], sumY-data[c][1])
            op[i]+=1

for tc in range(int(input())):
    N = int(input())
    data = []
    op = [N//2, N//2]
    for i in range(N):
        x, y = map(int, input().split())
        data.append((x, y))
    myMin = -1
    DFS(0, 0, 0)
    print("#{} {}".format(tc+1, myMin))


