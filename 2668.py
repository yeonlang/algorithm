import sys
sys.stdin = open("2668.txt","r")

n=int(input())
lst=[[i for i in range(1,n+1)],[]]
result=[]
check=[1 for _ in range(n)]
for _ in range(n):
    lst[1].append(int(input()))

for i in range(n):
    if lst[0][i] == lst[1][i]:
        result.append(lst[0][i])
        check[lst[0][i]-1] = 0

for j in range(n):
    if lst[0][j] == lst[1][lst[1][j]-1] and check[j]:
        check[lst[1][j]-1]=0
        result.append(lst[0][j])
        result.append(lst[1][j])

result.sort()
print(len(result))
for _ in result:
    print(_)




