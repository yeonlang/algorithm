import sys
sys.stdin = open("KMP.txt","r")

for tc in range(int(input())):
    pattern=list(input())
    l=len(pattern)
    Pi_table =[ -1 if i == 0 else 0 for i in range(l)]

    i = 0
    for j in range(1,l-1):
        if pattern[i] == pattern[j]:
            Pi_table[j+1] = Pi_table[j]+1
            i+= 1

        elif pattern[0] == pattern[j]:
            Pi_table[j+1] = 1
            i = 1

        else :
            Pi_table[j+1] = 0
            i = 0

    data = list(input())
    p = 0
    k = 0
    flag = 0

    while p+k < len(data) :
        if data[p+k] == pattern[k]:
            k += 1

        else:
            p += k - Pi_table[k]
            k = 0

        if k == l:
            flag = 1
            break

    if flag:
        print("#{} {}".format(tc+1,flag))
    else:
        print("#{} 0".format(tc+1))
