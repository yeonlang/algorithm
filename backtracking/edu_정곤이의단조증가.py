import sys
sys.stdin = open("정곤이의단조증가.txt","r")

from itertools import combinations as c
def judge(num):
    num1 = num%10
    num = num // 10

    while num:
        num2 = num%10
        if num1<num2:
            return False
        num1=num2
        num = num//10
    return True

for tc in range(int(input())):
    n = int(input())
    data = list(map(int,input().split()))
    visited = [0] * n
    my_max = -1
    for i,j in c(data,2):
        num=i*j
        if num>my_max and judge(num):
            my_max = num

    print("#{} {}".format(tc+1,my_max))



