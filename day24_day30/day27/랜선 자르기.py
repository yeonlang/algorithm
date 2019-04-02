import sys
sys.stdin = open("랜선자르기.txt")

N, num = map(int,input().split())
data = []
for _ in range(N):
    data.append(int(input()))

result = 0
start = 0
end = max(data)

while start<=end:
    mid = (start+end+1)//2
    cnt = 0

    for i in range(N):
        cnt += data[i]//mid

    if cnt >= num:
        result = mid
        start = mid + 1
    else :
        end = mid - 1

print(result)





