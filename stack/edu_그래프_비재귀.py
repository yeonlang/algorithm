import sys
sys.stdin =open("input3.txt","r")

my_map = [[0]*8 for i in range(8)]
visited = [0]*8
def DFS(here):
    stack=[here]
    while stack:
        now=stack.pop()
        visited[now] = True
        print(now)
        for next in range(8):
            if my_map[now][next] and not visited[next]:
                stack.append(next)

Data = list(map(int,input().split()))
n=len(Data)//2
for i in range(n):
    start= Data[i*2]
    stop = Data[i*2-1]
    my_map[start][stop] = 1
    my_map[stop][start] = 1

DFS(1)