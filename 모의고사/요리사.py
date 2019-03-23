import sys
sys.stdin = open("요리사.txt")

def BTK(choice,idx):
    global myMin
    if choice == N//2:
        data1,data2 = [],[]
        for i in range(N):
            if visited[i] == 0:
                data1.append(i)
            else :
                data2.append(i)
        A = 0
        B = 0
        for a in data1:
            for b in data1:
                if a != b:
                    A+= data[a][b]
        for a in data2:
            for b in data2:
                if a != b:
                    B+= data[a][b]
        temp = abs(A-B)
        if temp < myMin:
            myMin = temp
        return

    for i in range(idx+1,N):
        visited[i] = 1
        BTK(choice+1,i)
        visited[i] = 0

for tc in range(int(input())):
    N = int(input())
    data = [list(map(int,input().split())) for _ in range(N)]
    visited = [0]*N
    myMin = 987654321

    BTK(0,-1)
    print("#{} {}".format(tc+1,myMin))


