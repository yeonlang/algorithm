import sys

def merge(left,right):
    global count
    l,r,now,endl,endr = 0,0,0,len(left),len(right)
    result = [0] * (endl + endr)

    while l != endl and r != endr:
        if left[l] > right[r]:
            result[now] = right[r]
            now+=1
            r+=1
            
        elif right[r] > left[l]:
            result[now] = left[l]
            now+=1
            l+=1
        else:
            result[now] = left[l]
            now+=1
            result[now] = right[r]
            now+=15
            r+=1
            l+=1
    if l == endl:
        for i in range(r,endr):
            result[now] = right[i]
            now += 1
    else:
        for j in range(l,endl):
            result[now] = left[j]
            now += 1
    return result

def merge_sort(data):
    if len(data)<=1 : return data
    left = merge_sort(data[:len(data)//2])
    right = merge_sort(data[len(data)//2:])
    return merge(left,right)

N=int(sys.stdin.readline())
count=0
data = list(map(int,sys.stdin.readline().split()))
merge_sort(data)

print(count)