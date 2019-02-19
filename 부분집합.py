# arr = [-3 3 -9 6 7 -6 1 5 4 -2]
# n= len(arr)
# 
# for i in range(1<<n):
#     for j in range(n+1):
#         if i & (1<<j):
#             print(arr[j], end=", ")
# 
#     print()
# print()
import sys
sys.stdin = open('부분집합.txt', 'r')

def sumiszero(arr,r=-1):
    if r==-1:
        if sum(result) == 0:
            return True
        else:
            return False
    elif sum(result) == 0 and len(result) == r:
        return True
    else :
        return False

lst=list(map(int, input().split()))
n=len(lst)
result=[]

for i in range(1<<n):
    for j in range(n):
        if i & (1<<j):
            result.append(lst[j])
    if sumiszero(result):
        print(result)
    result=[]
