import sys
sys.stdin = open("수이어가기.txt","r")

n1=int(input())
my_max = 0
for n2 in range(1,n1+1):
    data=[n1]
    nxt = n2
    while nxt >= 0:
        data.append(nxt)
        nxt = data[-2]-data [-1]

    if len(data)>my_max:
        my_max = len(data)
        result = data[:]

print(my_max)
print(*result)
