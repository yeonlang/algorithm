import sys
sys.stdin = open("최소생산비용.txt")

def DFS(c,nowmin):
    global myMin
    if c == N:
        if nowmin<myMin:
            myMin = nowmin
    if nowmin>=myMin: return
    for x in range(N):
        if not visited[x]:
            visited[x] = 1
            DFS(c+1,nowmin+data[c][x])
            visited[x] = 0

for tc in range(int(input())):
    N = int(input())
    data = [ list(map(int,input().split())) for _ in range(N) ]
    visited = [0]*N
    myMin = 987654321

    DFS(0,0)
    print("#{} {}".format(tc+1,myMin))



#1 63
#2 78
#3 129
#4 163
#5 130
#6 151
#7 131
#8 156
#9 117
#10 151