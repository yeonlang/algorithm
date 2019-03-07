import sys

sys.stdin = open('baby_gin.txt', 'r') #파일에서 읽을때 사용
lst = list(map(int, input().split()))
count= [ 0 for i in range(max(lst)+1)]

run=0
tri=0

for i in lst:
    count[i]+=1

for j in range(len(count)):
    if count[j]>=3 :
        run+=1
        count[j]-=3

for k in range(1,len(count)-1):
    if count[k-1]>0 and count[k]>0 and count[k+1]>0:
        count[k-1] -= 1
        count[k] -= 1
        count[k+1] -= 1
        tri+=1

if count.count(0) == len(count):
    print(f"이것은 Baby gin 입니다. run = {run}, tri = {tri}")
else:
    print("이것은 Baby gin 이 아닙니다.")
