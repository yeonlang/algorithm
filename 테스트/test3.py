def DFS(c,idx):
    if result:
        print(result)
    for i in range(idx,N):
        result.append(i+1)
        DFS(c+1,i+1)
        result.pop()

N,K = 4,4
result = []
DFS(0,0)