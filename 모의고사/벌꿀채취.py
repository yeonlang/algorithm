import sys
sys.stdin = open("벌꿀채취.txt")

def sol(c,lst,idx,cnt,cntsum,s,D):
    global select
    if cnt>K or c>M: return

    if cntsum>D[0]:
        D[0] = cntsum
        select = s

    for i in range(idx,len(lst)):
        sol(c+1,lst,i+1,cnt+lst[i],cntsum+lst[i]**2,s,D)


def DFS(c,idx,lst,s,A):
    if c == 1:
        sol(0,lst,0,0,0,s,A)
        return A[0]

    temp = 0
    for i in range(idx,N**2):
        if i//N == (i+M-1)//N and not visited[i//N]:
            t1 = DFS(c+1,i+1,data[i//N][i%N:(i+M-1)%N+1],i//N,A)
            temp = max(temp,t1)
    return temp

for tc in range(int(input())):
    N,M,K = map(int,input().split())
    data = [list(map(int,input().split())) for _ in range(N)]
    A = [0]
    B = [0]
    visited = [0]*N
    select = -1
    result = 0
    result+=DFS(0,0,[],0,A)
    visited[select] = 1
    result+=DFS(0,0,[],0,B)
    print("#{} {}".format(tc+1,result))
