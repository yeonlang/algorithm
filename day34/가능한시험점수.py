import sys
sys.stdin = open("가능한시험점수.txt")

def DFS(c,cnt):
    if visited[c][cnt]: return
    visited[c][cnt] = 1
    result.add(cnt)
    if c>=N: return
    DFS(c+1,cnt+data[c])
    DFS(c+1,cnt)

for tc in range(int(input())):
    N = int(input())
    data = list(map(int,input().split()))
    visited = [[0]*10001 for _ in range(101)]
    result = set()
    DFS(0,0)
    print("#{} {}".format(tc+1,len(result)))
