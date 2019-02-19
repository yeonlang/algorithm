N=int(input())
arr=tuple(map(int,input().split()))
count=[ num for num in range(N)]
result=[0]*N

for i in range(N-1,-1,-1):
    index=i-arr[i]
    jump=count.pop(index)
    result[jump]=i+1

print(*result)