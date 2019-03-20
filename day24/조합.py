def BTK(n,r,choice=0,preidx=0):
    if choice == r:
        for i in range(n):
            if visited[i] != 0:
                print(i+1,end=" ")
        print()
        return
    for idx in range(preidx,n):
        if not visited[idx]:
            visited[idx]=1
            BTK(n,r,choice+1,idx)
            visited[idx]=0



n = 5
r = 3
visited = [0]*n
BTK(5,3)