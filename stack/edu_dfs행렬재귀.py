import sys
sys.stdin =open("input3.txt","r")

my_map = [[0]*8 for i in range(8)]
visited = [0]*8

def DFS(here):
    print(here)
    visited[here] = True

    for next in range(7):
        if my_map[here][next] and not visited[next]:
            DFS(next)

Data = list(map(int,input().split()))
n=len(Data)//2
for i in range(n):
    start= Data[i*2]
    stop = Data[i*2-1]
    my_map[start][stop] = 1
    my_map[stop][start] = 1

DFS(1)
