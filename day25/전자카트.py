import sys
sys.stdin = open("전자카트.txt")

def BTK(l,n):
    global myMin

    if l == n-1:
        ans = data[0][result[0]]
        for j in range(len(result)-1):
            ans += data[result[j]][result[j+1]]
        ans += data[result[-1]][0]
        if ans<myMin:
            myMin = ans
        return

    for x in range(1,n):
        if not visited[x]:
            visited[x] = 1
            result[l] = x
            BTK(l+1,n)
            result[l] = 0
            visited[x] = 0


for tc in range(int(input())):
    n = int(input())
    data = [ list(map(int,input().split())) for _ in range(n) ]
    visited = [0]*n
    result = [0]*(n-1)
    myMin = 987654321
    BTK(0,n)
    print("#{} {}".format(tc+1,myMin))
