def dfs(start):
    stack=[start]
    while stack:
        now=stack.pop()
        if result[now]==2:
            return
        result[now] += 1
        stack.append(lst[1][now]-1)

n=int(input())
lst=[[i for i in range(1,n+1)],[]]
result=[0 for _ in range(n)]
for _ in range(n):
    lst[1].append(int(input()))

for start in range(n):
    dfs(start)
    result=[ 2 if i==2 else 0 for i in result]

print(result.count(2))
for i in range(n):
    if result[i] == 2:
        print(i+1)