import sys
sys.stdin = open("시험감독.txt")

N = int(input())
data = list(map(int,input().split()))
s1,s2 = map(int,input().split())

cnt = 0
for i in range(N):
    temp = data[i] - s1
    if temp < 0:
        cnt+=1
        continue
    cnt+=1
    if temp%s2:
        cnt+=temp//s2+1
    else:
        cnt+=temp//s2

print(cnt)
