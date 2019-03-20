import sys
sys.stdin = open("이진수2.txt")

for tc in range(int(input())):
    n = float(input())
    i=1
    result = ''
    while i<13:
        if n-(2**-i)>0:
            result+='1'
            n-=(2**-i)
        elif n-(2**-i)==0:
            result+='1'
            break
        else:
            result += '0'
        i+=1
    if i == 13:
        print('#{} overflow'.format(tc+1))
    else:
        print("#{} {}".format(tc+1,result))