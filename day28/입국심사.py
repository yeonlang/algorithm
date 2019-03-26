import sys
sys.stdin = open("입국심사.txt")

N,K = map(int,input().split())
data = [0]*N
end = 0
for i in range(N):
    t = int(input())
    data[i] = t
    if t>end:
        end = t*K
start = 0

while start<=end:
    mid = (start+end+1)//2

    temp = 0
    for i in range(N):
        temp+=mid//data[i]

    if temp<K:
        start = mid+1
    else:
        end = mid-1

print(start)
