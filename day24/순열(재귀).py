def BTK(n,r,choice=0,i=0):
    if choice == r:
        print(result)
        return
    result[choice] = i+1
    for idx in range(n):
        if not visited[idx]:
            visited[idx]=1
            BTK(n,r,choice+1,idx+1)
            visited[idx]=0



n = 5
r = 3
visited = [0]*n
result = [0]*r
BTK(5,3)
