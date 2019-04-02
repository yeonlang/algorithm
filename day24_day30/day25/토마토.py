M,N,H = map(int,input().split())

data = [[ list(map(int,input().split())) for _ in range(N) ] for _ in range(H)]
print(data)
print(data[1][1][2])