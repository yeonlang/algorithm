import sys
sys.stdin = open("장난감조립.txt")

from collections import defaultdict
def DFS(num,val):
    if not dic[num]:
        result[num] += val
        return

    for i,j in dic[num]:
        DFS(i,j*val)

N = int(input())
M = int(input())
dic = defaultdict(lambda : [])

result = [0]*(N+1)
for i in range(M):
    num, sub, val = map(int,input().split())
    dic[num].append((sub,val))

for i,j in dic[N]:
    DFS(i, j)

for k in range(N):
    if result[k]:
        print(k,result[k])

