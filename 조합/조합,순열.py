# 순열
def permu1(c):
    if c == K:
        print(result)
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            result[c] = i
            permu1(c+1)
            visited[i]=0

# 중복 순열
def permu2(c):
    if c == K:
        print(result)
        return

    for i in range(N):
        result[c] = i
        permu2(c+1)

# 조합
def combi1(c,idx):
    if c == K:
        print(result)
        return

    for i in range(idx,N):
        result[c] = i
        combi1(c+1,i+1)

# 중복 조합
def combi2(c,idx):
    if c == K:
        print(result)
        return

    for i in range(idx,N):
        result[c] = i
        combi2(c+1,i)

# 부분집합
def subset(c,idx):
    print(result[:c])

    if c==K:
        return

    for i in range(idx,K):
        result[c] = i
        subset(c+1,i+1)

N = 5
K = 3
data = [1,2,3,4,5]
visited = [0]*N
result = [0,0,0]
combi1(0,0)
# combi2(0,0)
# permu1(0)
# permu2(0)
# subset(0,0)