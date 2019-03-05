import sys
sys.stdin = open("연산유효성검사.txt","r")

for tc in range(10):
    n = int(input())
    result = 1

    for i in range(n):
        data = list(input().split())
        if len(data) > 2:
            if not (data[1] == '+' or data[1] == '-' or data[1] == '*' or data[1] == '/'):
                result = 0

        if len(data) <= 2:
            if data[1] == '+' or data[1] == '-' or data[1] == '*' or data[1] == '/':
                result = 0

    print("#{} {}".format(tc+1,result))

