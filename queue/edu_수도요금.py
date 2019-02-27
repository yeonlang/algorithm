import sys
sys.stdin = open("수도요금.txt","r")

for tc in range(int(input())):
    p,q,r,s,w = map(int,input().split())
    #1리터당 요금 , 기본요금, 기준사용량, 초과요금, 월간사용량
    result=[]
    if w>r :
        result.append((w-r)*s+q)
    else :
        result.append(q)
    result.append(p*w)
    print(f'#{tc+1} {min(result)}')