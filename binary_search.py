import sys
sys.stdin = open('binary_search.txt', 'r')

def SequentialSearch(arr, value):
    lst = sorted(arr)
    n=len(lst)
    count=1

    for i in range(n):
        if lst[i] == value:
            print(f"count={count}")
            return True
        count+=1
    return False


def BinarySearch(arr,value):
    lst = sorted(arr)
    start=0
    end=len(lst)
    mid=(start+end)>>1
    count = 1

    while start-end<=0:
        if value == lst[mid]:
            print(f"count={count}")
            return True

        if lst[mid]>value:
            end = mid-1
            mid = (start+end) >> 1
        else :
            start = mid+1
            mid = (start+end) >> 1
        count+=1
    return False

arr=list(map(int,input().split()))

print(BinarySearch(arr,32))
print(SequentialSearch(arr,32))
