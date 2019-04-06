import sys
sys.stdin = open("스타트링크.txt")
from itertools import combinations as c

def BTK(choice,idx):
    global myMin
    if choice == N//2:
        A = []
        B = []
        for u in range(N):
            if visited[u]:
                A.append(u)
            else:
                B.append(u)
        r1 = 0
        r2 = 0
        for a,b in c(A,2):
            r1+=data[a][b]+data[b][a]
        for a,b in c(B,2):
            r2+=data[a][b]+data[b][a]
        temp = abs(r1-r2)
        if temp < myMin:
            myMin = temp
        return

    for i in range(idx,N):
        visited[i] = 1
        BTK(choice+1,i+1)
        visited[i] = 0

N = int(input())
data = [list(map(int,input().split())) for _ in range(N)]
visited = [0]*N
visited[0] = 1
myMin = 987654321
BTK(1,1)
print(myMin)