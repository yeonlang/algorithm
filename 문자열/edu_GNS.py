import sys
sys.stdin = open("GNS.txt","r")

for _ in range(int(input())):
    tc, n = map(str, input().split())
    n = int(n)
    data = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    my_str = {"ZRO":0, "ONE":0, "TWO":0, "THR":0, "FOR":0, "FIV":0, "SIX":0, "SVN":0, "EGT":0, "NIN":0}
    for i in input().split():
        my_str[i] += 1

    print(tc)
    for num in data:
        for i in range(my_str[num]):
            print(num,end=" ")


