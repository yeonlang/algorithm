import sys
sys.stdin = open("장난감조립.txt")

from collections import defaultdict

def DFS(num,val):
    if visited[num]: return visited[num]*val

    cnt = 0
    for i,j in dic[num]:
        cnt+=DFS(i,j)

    visited[num] = cnt
    return cnt*val

N = int(input())
M = int(input())
dic = defaultdict(lambda : [])

visited = [1 if 0<i< N else 0 for i in range(N+1)]
for i in range(M):
    num, sub, val = map(int,input().split())
    dic[num].append((sub,val))
    visited[num] = 0

count = 0
for i,j in dic[N]:
    count += DFS(i, j)




