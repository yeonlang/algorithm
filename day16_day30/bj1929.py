M,N = map(int,input().split())

data = [ i if i>1 else 0 for i in range(N+1)]

for i in range(2,N+1):
    if data[i] != 0:
        n = 2
        while i*n<len(data):
            data[i*n] = 0
            n+=1

for j in data[M:]:
    if j != 0:
        print(j)
