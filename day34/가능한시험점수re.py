import sys
sys.stdin = open("가능한시험점수.txt")

for tc in range(int(input())):
    N = int(input())
    data = list(map(int,input().split()))
    visited = [1]+[0]*(100*N)
    que = []
    cnt = 1
    for i in data:
        for j in range(100*N,-1,-1):
            if visited[j] and not visited[i+j]:
                visited[i+j] =1
                cnt += 1
    print("#{} {}".format(tc+1,cnt))