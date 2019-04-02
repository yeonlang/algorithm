import sys
sys.stdin = open("병합정렬.txt")

def merge(left,right):
    global cnt
    if left[-1]>right[-1]:
        cnt+=1
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
            now+=1
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

for tc in range(int(input())):
    N = int(input())
    data = list(map(int,input().split()))
    cnt = 0
    print("#{} {} {}".format(tc+1,merge_sort(data)[len(data)//2],cnt))
