import sys
sys.stdin = open("셀렉션소트.txt")

def SelectionSort(start,data):
    if start == l:
        return
    myMin = 987654321
    for i in range(start,l):
        if data[i]<myMin:
            idx = i
            myMin = data[i]
    data[start],data[idx] = data[idx],data[start]
    SelectionSort(start+1,data)


data = list(map(int,input().split()))
l = len(data)
SelectionSort(0,data)

print(data)