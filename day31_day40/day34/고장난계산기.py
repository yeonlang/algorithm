import sys
sys.stdin = open("고장난계산기.txt")



INF = 987654321
def count(n):
    cnt = 0
    while n>0:
        if not n%10 in button:
            return INF
        n = n//10
        cnt += 1
    return cnt

def solve(x):
    if dp[x]: return dp[x]
    dp[x] = count(x)
    for i in range(2,x//2):
        if x%i == 0:
            n1 = solve(i)
            n2 = solve(x//i)
            dp[x] = min(dp[x],n1+n2+1 if n1 != INF and n2 != INF else INF)
    return dp[x]

for tc in range(int(input())):
    data = list(map(int, input().split()))
    find = input()
    button = set()
    flag = False
    for i in range(len(data)):
        if data[i]:
            button.add(i)
    for i in range(len(find)):
        if not int(find[i]) in button:
            break
        if i == len(find)-1:
            flag = True
    if flag:
        print("#{} {}".format(tc+1,len(find)+1))
    else:
        find = int(find)
        dp = [0]*(find+10)
        myMin = solve(find)
        if myMin==INF:
            print("#{} {}".format(tc+1,-1))
        else:
            print("#{} {}".format(tc+1, myMin+1))



#1 6
#2 8
#3 7
#4 6
#5 10
#6 7
#7 -1
#8 11
#9 8
#10 4
#11 4
#12 -1
#13 6
#14 9
#15 2
#16 5
#17 -1
#18 4
#19 5
#20 9
#21 7
#22 2
#23 10
#24 9
#25 5
#26 6
#27 6
#28 15
#29 3
#30 -1
#31 5
#32 5
#33 4
#34 6
#35 6
#36 2
#37 2
#38 8
#39 8
#40 -1
#41 5
#42 9
#43 7
#44 2
#45 7
#46 5
#47 7
#48 8
#49 5
#50 5
#51 7
#52 7
#53 6
#54 2
#55 7
#56 6
#57 5
#58 7
#59 7
#60 6
#61 9
#62 7
#63 7
#64 7
#65 6
#66 11
#67 5
#68 12
#69 9
#70 6
#71 5
#72 7
#73 7
#74 5
#75 -1
#76 7
#77 6
#78 2
#79 5
#80 6
#81 -1
#82 -1
#83 -1
#84 2
#85 6
#86 11
#87 -1
#88 7
#89 7
#90 10
#91 7
#92 9
#93 2
#94 7
#95 9
#96 5
#97 7
#98 6
#99 6
#100 4



