import sys
sys.stdin = open("올림픽 종목 투표.txt")

def DFS(c):
    if c == M: return
    for i in range(N):
        if B[c]>=A[i]:
            cnt[i]+=1
            DFS(c+1)
            break

for tc in range(int(input())):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    cnt = [0]*N
    DFS(0)
    print("#{} {}".format(tc+1,cnt.index(max(cnt))+1))

