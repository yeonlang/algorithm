import sys
sys.stdin = open("연산.txt")

from collections import deque
def ispass(N): return True if 0<N<=1000000 else False
def BFS(start):
    que = deque([start])
    visited[start] = 1
    while que:
        now = que.popleft()
        if now == M: return
        for i in range(4):
            if d[i] == '*':
                nxt = now*2
            else:
                nxt = now+d[i]
            if ispass(nxt) and not visited[nxt]:
                visited[nxt] = visited[now]+1
                que.append(nxt)


for tc in range(int(input())):
    N, M = map(int,input().split())
    visited = [0]*1000001
    d = [-1,1,'*',-10]
    BFS(N)
    print("#{} {}".format(tc+1,visited[M]-1))