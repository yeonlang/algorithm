def btk(c,idx):
    if c == K:
        print(result)
        return

    for i in range(idx,N):
        result.append(data[i])
        btk(c+1,i+1)
        result.pop()

N = 6
K = 3
data = [1,2,3,4,5,6]
visited = set()
result = []
btk(0,0)