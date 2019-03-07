import sys
sys.stdin = open("농작물.txt","r")

for tc in range(int(input())):
    n = int(input())
    data = [ list(map(int,input())) for _ in range(n)]

    result = 0
    mid=n//2
    for y in range(n):
        if y<=mid:
            for x in range(mid-y,mid+y+1):
                result+=data[y][x]

        if y>mid:
            t = y-mid
            for x in range(t,n-t):
                result += data[y][x]

    print("#{} {}".format(tc+1,result))

    # 1 23
    # 2 1190
    # 3 946
    # 4 112
    # 5 1886
    # 6 3000
    # 7 1032
    # 8 1330
    # 9 939
    # 10 2960
    # 11 547
    # 12 3016
    # 13 1712
    # 14 2049
    # 15 1294
    # 16 354
    # 17 1634
    # 18 1901
    # 19 2518
    # 20 1750
    # 21 2144
    # 22 940
    # 23 0
    # 24 1712
    # 25 1685
    # 26 559
    # 27 874
    # 28 75
    # 29 139
    # 30 3
    # 31 13
    # 32 331
    # 33 2646
    # 34 1531
    # 35 156
    # 36 1663
    # 37 934
    # 38 1725
    # 39 107
    # 40 2291
    # 41 84
    # 42 590
    # 43 31
    # 44 1351
    # 45 1364
    # 46 1187
    # 47 1059
    # 48 1771
    # 49 1228
    # 50 2065
