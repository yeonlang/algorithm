import sys
sys.stdin = open('counting_sort.txt', 'r') #파일에서 읽을때 사용

lst = list(map(int, input().split()))
temp = [ 0 for _ in range(len(lst))]
count= [ 0 for i in range(max(lst)+1)]

for i in lst:
    count[i]+=1

for j in range(1,len(count)):
    count[j]+=count[j-1]

for i in lst:
    count[i]-=1
    temp[count[i]]=i

print(temp)
