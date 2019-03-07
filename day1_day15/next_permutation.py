import sys

# def next_permutation(Data):
#     cand1 = 0
#     for now in range(len(Data)-1):
#         if Data[now]<Data[now+1]:
#             cand1=now
#     if cand1 == 0 :
#         return False
#
#     cand2 = len(Data) -1
#     while Data[cand1] > Data[cand2]:
#         cand2 -= 1
#
#     Data[cand1], Data[cand2] = Data[cand2], Data[cand1]
#
#     Data[cand1+1:] = Data[:cand1:-1]
#     return(Data)

sys.stdin = open('next_permutation.txt', 'r') #파일에서 읽을때 사용

Data = list(map(int, input().split()))


cand1=0
cand2=0
i = len(Data)

for j in Data[::-1]:
    i-=1
    if i == 0:
        break
    if j > Data[i-1]:
        cand1 = Data[i-1]
        index1= i-1
        for cand2 in Data[:i-1:-1]:
            if cand2 > cand1:
                index2=Data.index(cand2)
                Data[index1], Data[index2] = Data[index2], Data[index1]
                Data[index1+1::]=Data[:index1:-1]
                break
        break

print(" ".join(map(str,Data)))

