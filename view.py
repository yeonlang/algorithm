for tc in range(10):
    a=input()
    lst = list(map(int,input().split()))
    count=0

    for i in range(2,len(lst)-2):
        value = lst[i]
        while value>lst[i-1] and value>lst[i-2] and value>lst[i+1] and value>lst[i+2]:
            count+=1
            value-=1

    print(f"#{tc+1} {count}")
