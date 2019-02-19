import sys

sys.stdin = open('BubbleSort.txt', 'r') #파일에서 읽을때 사용
Data = list(map(int, input().split()))
l=len(Data)

while l-1 :
    for i in range(l):
        if i == l-1:
            break
        if Data[i] > Data[i+1]:
            Data[i], Data[i+1] = Data[i+1], Data[i]
    l-=1

print(Data)
