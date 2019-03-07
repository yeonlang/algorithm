import sys

sys.stdin = open('gravity.txt', 'r') #파일에서 읽을때 사용
Data = list(map(int, input().split()))
my_max = 0
size = len(Data)

D = {i: 0 for i in range(1, size+1)}

for j, i in enumerate(Data):
    for k in range(1, i+1):
        if D[k] == 0:
            D[k] = size - j - 1
        else:
            D[k] = D[k]-1

for r in D.values():
    if r > my_max:
        my_max = r

print(my_max)



# for now in range(size):
#     jumpcnt = size-now -1
#     for next in range(now+1,size):
#         if Data[next] >= Data[now]:
#             jumpcnt -=1
#         if jumpcnt > max:
#             max=jumpcnt


