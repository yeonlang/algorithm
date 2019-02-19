import sys
sys.stdin = open("sw1259.txt","r")

for tc in range(int(input())):
    n=int(input())
    lst=list(map(int,input().split()))
    head,tail,check,result=[],[],[],[]

    for i in range(n):
        head.append(lst[2*i])
        tail.append(lst[2*i+1])

    for j in range(n):
        if head[j] in tail:
            check.append(head[j])

    for k in check:
        k_index=head.index(k)
        result.append((head.pop(k_index), tail.pop(k_index)))

    head=head[0]
    tail=tail[0]
    count = len(result)

    print(f"#{tc+1}",head,tail, end=" ")
    while count>0:
        for i in range(len(result)):
            if result[i][0] == tail:
                head,tail = result[i][0],result[i][1]
                count-=1
                print(head, tail, end=" ")
    print()





