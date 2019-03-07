import sys

sys.stdin = open('counting_sort.txt', 'r') #파일에서 읽을때 사용

Data = list(map(int, input().split()))

my_max = Data[0]
max_index= -1

for i,j in enumerate(Data):
    if j>my_max:
        my_max=j
        max_index = i

print(my_max, max_index)
