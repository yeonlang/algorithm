def BTK(c,preidx,r):
    if c == r:
        result = []
        for j in range(len(visited)):
            if visited[j] != 0:
                result += [data[j]]
        if sum(result) == 0:
            print(result)
        return
    for idx in range(preidx,len(data)):
        if not visited[idx]:
            visited[idx]=1
            BTK(c+1,idx,r)
            visited[idx]=0




data = [-1,3,-9,6,7,-6,1,5,4,-2]
visited = [0]*len(data)
BTK(0,0,4)

