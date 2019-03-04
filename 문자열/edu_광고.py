import sys
sys.stdin = open("KMP.txt","r")

def fail(pattern):
    l = len(pattern)
    i = 0
    ans = [0 for i in range(l+1)]
    for j in range(1,l):
        if pattern[i] == pattern[j]:
            ans[j+1] = ans[j]+1
            i+= 1

        elif pattern[0] == pattern[j]:
            ans[j+1] = ans[j]
            i = 1

        else :
            ans[j+1] = 0
            i = 0

    return ans

n = int(input())
Pi = list(input())
Pi_table = fail(Pi)
print(Pi_table)
print(n-Pi_table[n])
