import sys
sys.stdin=open("2607.txt",'r')

lst=[]
result=0

for t in range(int(input())):
    lst.append(input())

n=len(lst)
str1 = { chr(key):0 for key in range(65,91)}

for _ in lst[0]:
    str1[_] += 1

for i in range(1,n):
    check = dict.copy(str1)
    count = [0, 0]
    for j in lst[i]:
        check[j] -= 1
    for k in check:
        if check[k] != 0 and  check[k] != 1 and check[k] != (-1):
            count[0]=2
            break
        elif check[k] == 1:
            count[0] += 1
        elif check[k] == (-1):
            count[1] += 1
    if count[0]<=1 and count[1]<=1:
        result+=1


print(result)