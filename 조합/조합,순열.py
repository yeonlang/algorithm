# 순열
def permu1(c):
    if c == K:
        print(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result.append(data[i])
            permu1(c+1)
            result.pop()
            visited[i]=0

# 중복 순열
def permu2(c):
    if c == K:
        print(result)
        return

    for i in range(N):
        result.append(data[i])
        permu2(c+1)
        result.pop()

# 조합
def combi1(c,idx):
    if c == K:
        print(result)
        return

    for i in range(idx,N):
        result.append(data[i])
        combi1(c+1,i+1)
        result.pop()

# 중복 조합
def combi2(c,idx):
    if c == K:
        print(result)
        return

    for i in range(idx,N):
        result.append(data[i])
        combi2(c+1,i)
        result.pop()

N = 5
K = 3
data = [1,2,3,4,5]
visited = [0]*N
result = []
combi1(0,0)
# combi2(0,0)
# permu1(0)
# permu2(0)