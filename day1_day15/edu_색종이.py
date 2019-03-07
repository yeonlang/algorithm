import sys
sys.stdin=open("색종이.txt","r")

n = int(input())
x_size = [0] * (n+1)
y_size = [0] * (n+1)
data = [0] * n

for i in range(1,n+1):
    x_size[i],y_size[i] = map(int, input().split())

for j in range(n):
    if x_size[j+1] > y_size[j+1]:
        data[j] = (x_size[j+1],y_size[j+1])
    else:
        data[j] = (y_size[j+1],x_size[j+1])

data.sort(key = lambda x:x[1], reverse = True)

result = []
result.append(data[0])
for i in range(1,n):
    if data[i][0] < result[-1][0]:
        result.append(data[i])

print(len(result))