import sys
sys.stdin = open("다각형.txt","r")

def R_data():
    result=[]
    for i in range(1,n+1):
        if data[-i] == 1:
            result.append(3)
        elif data[-i] == 2:
            result.append(4)
        elif data[-i] == 3:
            result.append(1)
        elif data[-i] == 4:
            result.append(2)
    return result

def shift(arr):
    for i in range(1,len(arr)):
        arr[-i],arr[-i-1] = arr[-i-1],arr[-i]

# arr1 = 회전시켜 비교할 데이터 , arr2 = 비교대상 데이터
def judge(arr1,arr2):
    global flag
    for i in range(n):
        if arr1 == arr2:
            flag = True
        shift(arr1)

n = int(input())
data = list(map(int,input().split()))
r_data = R_data()
result = []

for tc in range(int(input())):
    case = list(map(int,input().split()))
    flag = False
    judge(data[:],case)
    judge(r_data[:],case)
    if flag:
        result.append(case)

l_result = len(result)
print(l_result)
for i in range(l_result):
    print(*result[i])


