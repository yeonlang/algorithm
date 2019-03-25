
def swap(arr, a, b) : arr[a],arr[b] = arr[b],arr[a]
def quick_sort(arr,left,right):
    if left >= right: return
    p = arr[left]
    low, high = left,right
    while low < high:
        while arr[low] <= p and low<right: low+=1
        while arr[high] > p : high-=1

        if low<high : swap(arr,low,high)

    swap(arr,left,high)

    quick_sort(arr,left,high-1)
    quick_sort(arr,high+1,right)

data1 = [11,45,23,81,28,34]
data2 = [11,45,22,81,23,34,99,22,17,8]
data3 = [1,1,1,1,1,0,0,0,0,0]

quick_sort(data1,0,len(data1)-1)
quick_sort(data2,0,len(data2)-1)
quick_sort(data3,0,len(data3)-1)

print(data1)
print(data2)
print(data3)




