import sys
sys.stdin = open("랜선자르기.txt")

N, num = map(int,input().split())
data = []
for _ in range(N):
    data.append(int(input()))
data.sort()

value = data[1]//2
start = 0
end = data[1]
while start<=end:
    mid = (start+value)//2

    for i in range(N):
        result += data[i]//value

    if result == num:
        if start>=end or start == value or value == end:
            break
        start = value
    elif result>num:
        start = (start+value)//2
    elif result<num:
        end = (value+end)//2
    value = (start + end) // 2

print(value)





