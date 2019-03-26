import sys
sys.stdin = open("퇴사.txt")

def DFS(c,cnt):
    global myMax
    if c > N: return
    if cnt>myMax:
        myMax = cnt

    for i in range(c,N):
        DFS(i+data[i][0],cnt+data[i][1])

N = int(input())
data = []
for i in range(N):
    T,P = map(int,input().split())
    data.append((T,P))
myMax = 0
DFS(0,0)
print(myMax)


