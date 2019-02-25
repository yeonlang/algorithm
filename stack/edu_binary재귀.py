import sys
sys.stdin = open('binary_search.txt', 'r')

def BinarySearch(start,end,value):
    global count
    count+=1
    mid=(start+end)>>1
    if arr[mid] == value:
        return True
    if start == end:
        return False
    elif arr[mid] > value :
        return BinarySearch(start,mid-1,value)
    elif arr[mid] < value :
        return BinarySearch(mid+1,end,value)


arr=list(map(int,input().split()))
arr.sort()
count = 0

print(BinarySearch(0,len(arr)-1,32),count)
