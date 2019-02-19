import sys
sys.stdin = open("sw4837.txt","r")

def find(N,K):
    count=0
    for i in range(1<<12):
        result=[]
        for j in range(12):
            if i & (1 << j):
                result.append(A[j])
        if len(result) == N and sum(result) == K:
            count+=1
    return count

A=[1,2,3,4,5,6,7,8,9,10,11,12]
for tc in range(int(input())):
    N, K = map(int, input().split())
    print(f"#{tc+1} {find(N,K)}")
