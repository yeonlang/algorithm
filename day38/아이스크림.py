import sys
sys.stdin = open("아이스크림.txt")

def DFS(c,idx):
    global cnt
    if c == 3:
        if (result[0],result[1]) in data or (result[0],result[2]) in data or (result[1],result[2])in data:
            return
        cnt+=1
        return

    for i in range(idx,N+1):
        result[c] = i
        DFS(c+1,i+1)



N,M = map(int,input().split())
data = []
apd = data.append
for i in range(M):
    a,b = map(int,input().split())
    apd((a,b))
result = [0]*N
cnt = 0
result = [0,0,0]
DFS(0,1)
print(cnt)
