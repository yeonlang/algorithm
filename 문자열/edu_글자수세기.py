import sys
sys.stdin = open("글자수세기.txt","r")

for tc in range(int(input())):
    pattern = set(input())
    data = list(input())
    result = { key:0 for key in pattern }
    for i in range(len(data)):
        if data[i] in result:
            result[data[i]]+=1

    x=list(result.values())
    print("#{} {}".format(tc+1,max(x)))